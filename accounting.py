import arcadeplus

WIDTH = 1000
HEIGHT = 690

_left = 0
_right = WIDTH
_bottom = 0
_top = HEIGHT

scroll_down = False
scroll_up = False
save = False
coa_save_num = 1
tb_save_num = 1
is_save_num = 1

home_page = True
chart_of_accounts = False
trial_balance = False
income_statement = False
main_menu = False

home_page_press = False
chart_of_accounts_press = False
trial_balance_press = False
income_statement_press = False

interval5 = False
interval1 = False
interval_selection_done = False
interval_selection_page = False

month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

asset_name = []
asset_value = []
asset_cr_dr = []

a_r_p_name = []
a_r_p_value = []
a_r_p_dc = []
dc_ppl = []
a_r_p_2d = []
a_r_p_dict = {}
bank = True

liability_name = []
liability_value = []
liability_cr_dr = []

capital_name = []
capital_value = []
capital_cr_dr = []

drawing_name = []
drawing_value = []
drawing_cr_dr = []

revenue_name = []
revenue_value = []
revenue_cr_dr = []

expense_name = []
expense_value = []
expense_cr_dr = []

tb_name = False
tb_title = False
tb_date = False
tb_col1 = False
tb_col2 = False
tb_name_x = 400
tb_title_x = 400
tb_date_x = 400
c_tb_col1x = 400
tb_col1x = 410
c_tb_col2x = 600
tb_col2x = 610

is_name = False
is_title = False
is_date = False
is_col1 = False
is_col2 = False
is_name_x = 400
is_title_x = 400
is_date_x = 400
c_is_col1x = 400
is_col1x = 410
c_is_col2x = 600
is_col2x = 610

mouse_press = False
mouse_x = 0
mouse_y = 0

def setup():
    arcadeplus.open_window(WIDTH, HEIGHT, "Accounting Helper")
    arcadeplus.set_background_color(arcadeplus.color.DARK_GREEN)
    arcadeplus.schedule(update, 1/60)

    # Override arcade window methods
    window = arcadeplus.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press
    window.on_mouse_release = on_mouse_release
    window.on_mouse_motion = on_mouse_motion
    window.set_viewport = set_viewport

    arcadeplus.run()


def update(delta_time):
    pass


def on_draw():
    global _top, _bottom, tb_name, tb_date, tb_title, tb_col1, tb_col2
    arcadeplus.start_render()
    # Draw in here...
    if home_page:
        arcadeplus.set_viewport(0, WIDTH, 0, HEIGHT)
        _top = HEIGHT
        _bottom = 0
        tb_name = False
        tb_date = False
        tb_title = False
        tb_col1 = False
        tb_col2 = False
        home()
    elif chart_of_accounts:
        if interval_selection_done:
            make_chart_of_accounts()
        else:
            interval_selection()
    elif trial_balance:
        make_trial_balance()
    elif income_statement:
        make_income_statement()


def on_key_press(key, modifiers):
    global main_menu, scroll_down, scroll_up, save, tb_col2x, c_tb_col2x
    global tb_date_x, tb_name_x, tb_title_x, tb_col1x, c_tb_col1x
    global is_name_x, is_date_x, is_title_x, is_col1x, is_col2x, c_is_col1x, c_is_col2x
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = True
    if not home_page and not interval_selection_page:
        if key == arcadeplus.key.DOWN:
            scroll_down = True
        if key == arcadeplus.key.UP:
            scroll_up = True
        if key == arcadeplus.key.S:
            save = True
    if trial_balance:
        if key == arcadeplus.key.R:
            tb_name_x = 400
            tb_date_x = 400
            tb_title_x = 400
            tb_col1x = 410
            tb_col2x = 610
            if currency_pos == 'before':
                c_tb_col1x = 400
                c_tb_col2x = 600
            else:
                c_tb_col1x = 410
                c_tb_col2x = 610
        if key == arcadeplus.key.LEFT:
            if tb_name and tb_name_x > 0:
                tb_name_x -= 5
            elif tb_title and tb_title_x > 0:
                tb_title_x -= 5
            elif tb_date and tb_date_x > 0:
                tb_date_x -= 5
            elif tb_col1 and 396 <= tb_col1x:
                tb_col1x -= 5
                c_tb_col1x -= 5
            elif tb_col2 and 596 <= tb_col2x:
                tb_col2x -= 5
                c_tb_col2x -= 5
        if key == arcadeplus.key.RIGHT:
            if tb_name and tb_name_x < 1000:
                tb_name_x += 5
            elif tb_title and tb_title_x < 1000:
                tb_title_x += 5
            elif tb_date and tb_date_x < 1000:
                tb_date_x += 5
            elif tb_col1 and tb_col1x <= 595:
                tb_col1x += 5
                c_tb_col1x += 5
            elif tb_col2 and tb_col2x <= 995:
                tb_col2x += 5
                c_tb_col2x += 5
    if income_statement:
        if key == arcadeplus.key.R:
            is_name_x = 400
            is_date_x = 400
            is_title_x = 400
            is_col1x = 410
            is_col2x = 610
            if currency_pos == 'before':
                c_is_col1x = 400
                c_is_col2x = 600
            else:
                c_is_col1x = 410
                c_is_col2x = 610
        if key == arcadeplus.key.LEFT:
            if is_name and is_name_x > 0:
                is_name_x -= 5
            elif is_title and is_title_x > 0:
                is_title_x -= 5
            elif is_date and is_date_x > 0:
                is_date_x -= 5
            elif is_col1 and 396 <= is_col1x:
                is_col1x -= 5
                c_is_col1x -= 5
            elif is_col2 and 596 <= is_col2x:
                is_col2x -= 5
                c_is_col2x -= 5
        if key == arcadeplus.key.RIGHT:
            if is_name and is_name_x < 1000:
                is_name_x += 5
            elif is_title and is_title_x < 1000:
                is_title_x += 5
            elif is_date and is_date_x < 1000:
                is_date_x += 5
            elif is_col1 and is_col1x <= 595:
                is_col1x += 5
                c_is_col1x += 5
            elif is_col2 and is_col2x <= 995:
                is_col2x += 5
                c_is_col2x += 5


def on_key_release(key, modifiers):
    global main_menu, home_page, chart_of_accounts
    global trial_balance, income_statement, save
    global scroll_up, scroll_down, interval_selection_page
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = False
            home_page = True
            chart_of_accounts = False
            trial_balance = False
            income_statement = False
            interval_selection_page = False
    if not home_page and not interval_selection_page:
        if key == arcadeplus.key.DOWN:
            scroll_down = False
        if key == arcadeplus.key.UP:
            scroll_up = False
        if key == arcadeplus.key.S:
            save = False
    if home_page:
        scroll_down = False
        scroll_up = False


def on_mouse_press(x, y, button, modifiers):
    global mouse_press
    if button == arcadeplus.MOUSE_BUTTON_LEFT:
        mouse_press = True


def on_mouse_release(x, y, button, modifiers):
    global mouse_press
    if button == arcadeplus.MOUSE_BUTTON_LEFT:
        mouse_press = False


def on_mouse_motion(x, y, dx, dy):
    global mouse_x, mouse_y
    mouse_x = x
    mouse_y = y


def set_viewport(left, right, bottom, top):
    global _left, _right, _bottom, _top
    _left = left
    _right = right
    _bottom = bottom
    _top = top


def home():
    arcadeplus.set_background_color(arcadeplus.color.DARK_GREEN)
    arcadeplus.draw_text('Accounting Helper', 340, 530, arcadeplus.color.BLUE_VIOLET, 35, font_name='calibri')
    chart_of_accounts_bttn(WIDTH/2, 400, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    trial_balance_bttn(WIDTH/2, 350, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    income_statement_bttn(WIDTH/2, 300, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    arcadeplus.draw_text('Chart of Accounts', 430, 388, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Trial Balance', 450, 338, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Income Statement', 428, 288, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Press esc to come back to this menu from the sub menus', 80, 100, arcadeplus.color.BLUE_SAPPHIRE, 30, font_name='calibri')


def chart_of_accounts_bttn(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global chart_of_accounts_press, home_page, chart_of_accounts, interval_selection_done
    global interval1, interval5
    left = centre_x - width/2
    right = centre_x + width/2
    top = centre_y + height/2
    bottom = centre_y - height/2
    if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
        chart_of_accounts_press = True
    elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
        if chart_of_accounts_press:
            chart_of_accounts_press = False
            interval_selection_done = False
            interval5 = False
            interval1 = False
            chart_of_accounts = True
            home_page = False
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        chart_of_accounts_press = False


def trial_balance_bttn(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global trial_balance_press, trial_balance, home_page
    left = centre_x - width/2
    right = centre_x + width/2
    top = centre_y + height/2
    bottom = centre_y - height/2
    if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
        trial_balance_press = True
    elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
        if trial_balance_press:
            trial_balance_press = False
            trial_balance = True
            home_page = False
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        trial_balance_press = False


def income_statement_bttn(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global home_page, income_statement_press, income_statement
    left = centre_x - width/2
    right = centre_x + width/2
    top = centre_y + height/2
    bottom = centre_y - height/2
    if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
        income_statement_press = True
    elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
        if income_statement_press:
            income_statement_press = False
            income_statement = True
            home_page = False
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        income_statement_press = False


def interval_selection():
    global interval_selection_page
    interval_selection_page = True
    arcadeplus.set_background_color(arcadeplus.color.DARK_BLUE_GRAY)
    arcadeplus.draw_text('Select the interval in which you want your account numbers to go up by.', 70, 530, arcadeplus.color.WHITE, 24, font_name='calibri')
    account_interval1(WIDTH/2, 390, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    account_interval5(WIDTH/2, 300, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    arcadeplus.draw_text('1s', 488, 379, arcadeplus.color.WHITE, 16, font_name='calibri')
    arcadeplus.draw_text('5s', 488, 289, arcadeplus.color.WHITE, 16, font_name='calibri')


def account_interval5(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global interval5, interval_selection_done, interval_selection_page
    if not interval_selection_done:
        left = centre_x - width/2
        right = centre_x + width/2
        top = centre_y + height/2
        bottom = centre_y - height/2
        if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
            arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
            interval5 = True
        elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
            arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
            if interval5:
                interval_selection_done = True
                interval_selection_page = False
        else:
            arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
            interval_selection_done = False
            interval5 = False
            interval_selection_page = True


def account_interval1(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global interval1, interval_selection_done, interval_selection_page
    left = centre_x - width/2
    right = centre_x + width/2
    top = centre_y + height/2
    bottom = centre_y - height/2
    if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
        interval1 = True
    elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
        if interval1:
            interval_selection_done = True
            interval_selection_page = False
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        interval_selection_done = False
        interval1 = False
        interval_selection_page = True


def capitalize(acct_type_name):
    copy = acct_type_name.copy()
    acct_type_name.clear()
    for n in range(len(copy)):
        if 'A/R' not in copy[n] and 'A/P' not in copy[n] and 'HST' not in copy[n]:
            if copy[n].find(' ') == -1:
                acct_type_name.append(copy[n].capitalize())
            else:
                separate = copy[n].split(' ')
                account = ''
                for i in range(len(separate)):
                    account += separate[i].capitalize()
                    if i != len(separate) - 1:
                        account += ' '
                acct_type_name.append(account)
        else:
            acct_type_name.append(copy[n])


def liquidity_assets():
    global asset_name, asset_value, asset_cr_dr, bank
    try:
        i = asset_name.index('bank')
        account_name = asset_name.pop(i)
        account_value = asset_value.pop(i)
        account_dr_cr = asset_cr_dr.pop(i)
        asset_name.insert(0, account_name)
        asset_value.insert(0, account_value)
        asset_cr_dr.insert(0, account_dr_cr)
        bank = True
    except:
        bank = False
    liquidity_ar_ap(asset_name, asset_value, asset_cr_dr, 'a/r', 'A/R')
    capitalize(asset_name)


def liquidity_liabilities():
    global liability_name, liability_value, liability_cr_dr, count
    liability_liquidity = ['hst payable', 'hst recoverable', 'bank loan', 'mortgage']
    bank = False
    liquidity_ar_ap(liability_name, liability_value, liability_cr_dr, 'a/p', 'A/P')
    for n in range(len(liability_liquidity)):
        try:
            i = liability_name.index(liability_liquidity[n])
            account_name = liability_name.pop(i)
            account_value = liability_value.pop(i)
            account_dr_cr = liability_cr_dr.pop(i)
            if account_name == 'hst payable':
                liability_name.insert(count, 'HST Payable')
            elif account_name == 'hst recoverable':
                liability_name.insert(count, 'HST Recoverable')
            else:
                liability_name.insert(count, account_name)
            liability_value.insert(count, account_value)
            liability_cr_dr.insert(count, account_dr_cr)
            count += 1
        except:
            pass
    capitalize(liability_name)


def sort_liquidity_cap_draw(acct_t_name, acct_t_value, acct_t_dc, text):
    global a_r_p_dict, a_r_p_name, a_r_p_value
    global a_r_p_dc, a_r_p_2d
    rem_times = 0
    for n in range(len(acct_t_name)+rem_times):
        a_r = acct_t_name[n-rem_times]
        comma = a_r.rfind(',')
        debtor = a_r[:comma]
        semi_colon = debtor.find(';')
        capitalize_list = debtor.split(';')
        debtor = ''
        for i in range(len(capitalize_list)):
            debtor += capitalize_list[i].capitalize()
            if i != len(capitalize_list) - 1:
                debtor += ' '
        capitalize_list.clear()
        a_r_p_name.append(debtor)
        acct_t_name.pop(n-rem_times)
        a_r_p_value.append(acct_t_value[n-rem_times])
        a_r_p_dc.append(acct_t_dc[n-rem_times])
        acct_t_value.pop(n-rem_times)
        acct_t_dc.pop(n-rem_times)
        rem_times += 1
    if len(a_r_p_name) != 0:
        for n in range(len(a_r_p_name)):
            a_r_p_2d.append([a_r_p_value[n], a_r_p_dc[n]])
        for n in a_r_p_name:
            for x, y in a_r_p_2d:
                a_r_p_dict[n] = [x, y]
                a_r_p_2d.remove([x, y])
                break
        alphabetical_a_r_p = sorted(a_r_p_dict)
        a_r_p_name.clear()
        a_r_p_value.clear()
        a_r_p_dc.clear()
        for n in alphabetical_a_r_p:
            a_r_p_value.append(a_r_p_dict[n][0])
            a_r_p_dc.append(a_r_p_dict[n][1])
            space = n.find(' ')
            debtor = n[space+1:] + ' ' + n[:space]
            a_r_p_name.append(debtor)
        for n in range(len(a_r_p_name)):
            acct_t_name.insert(i, f'{a_r_p_name[n]}, {text}')
            acct_t_value.insert(i, a_r_p_value[n])
            acct_t_dc.insert(i, a_r_p_dc[n])
            i += 1
        a_r_p_dict.clear()
        a_r_p_name.clear()
        a_r_p_value.clear()
        a_r_p_dc.clear()
        a_r_p_2d.clear()
        dc_ppl.clear()


def liquidity_ar_ap(acct_t_name, acct_t_value, acct_t_dc, text, text2):
    global a_r_p_dict, a_r_p_name, a_r_p_value
    global a_r_p_dc, a_r_p_2d, dc_ppl, count
    rem_times = 0
    for n in range(len(acct_t_name)+rem_times):
        if text in acct_t_name[n-rem_times]:
            a_r = acct_t_name[n-rem_times]
            debtor = a_r[4:]
            semi_colon = debtor.find(';')
            if semi_colon == -1:
                if debtor.find(' ') == -1:
                    a_r_p_name.append(debtor.capitalize())
                else:
                    capitalize_list = debtor.split(' ')
                    debtor = ''
                    for i in range(len(capitalize_list)):
                        debtor += capitalize_list[i].capitalize()
                        if i != len(capitalize_list) - 1:
                            debtor += ' '
                    a_r_p_name.append(debtor)
                    capitalize_list.clear()
            else:
                capitalize_list = debtor.split(';')
                debtor = ''
                for i in range(len(capitalize_list)):
                    debtor += capitalize_list[i].capitalize()
                    if i != len(capitalize_list) - 1:
                        debtor += ' '
                capitalize_list.clear()
                a_r_p_name.append(debtor)
                dc_ppl.append(debtor)
            acct_t_name.pop(n-rem_times)
            a_r_p_value.append(acct_t_value[n-rem_times])
            a_r_p_dc.append(acct_t_dc[n-rem_times])
            acct_t_value.pop(n-rem_times)
            acct_t_dc.pop(n-rem_times)
            rem_times += 1
    if len(a_r_p_name) != 0:
        for n in range(len(a_r_p_name)):
            a_r_p_2d.append([a_r_p_value[n], a_r_p_dc[n]])
        for n in a_r_p_name:
            for x, y in a_r_p_2d:
                a_r_p_dict[n] = [x, y]
                a_r_p_2d.remove([x, y])
                break
        alphabetical_a_r_p = sorted(a_r_p_dict)
        a_r_p_name.clear()
        a_r_p_value.clear()
        a_r_p_dc.clear()
        for n in alphabetical_a_r_p:
            a_r_p_value.append(a_r_p_dict[n][0])
            a_r_p_dc.append(a_r_p_dict[n][1])
            if n in dc_ppl:
                space = n.find(' ')
                debtor = n[space+1:] + ' ' + n[:space]
                a_r_p_name.append(debtor)
            else:
                a_r_p_name.append(n)
    if bank:
        i = 1
    else:
        i = 0
    count = len(a_r_p_name)
    for n in range(count):
        acct_t_name.insert(i, f'{text2} {a_r_p_name[n]}')
        acct_t_value.insert(i, a_r_p_value[n])
        acct_t_dc.insert(i, a_r_p_dc[n])
        i += 1
    a_r_p_dict.clear()
    a_r_p_name.clear()
    a_r_p_value.clear()
    a_r_p_dc.clear()
    a_r_p_2d.clear()
    dc_ppl.clear()


def make_chart_of_accounts():
    global first_line_y, _top, _bottom, coa_save_num
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    if interval1:
        starting_num = 1
    else:
        starting_num = 5
    first_line_y = 660
    make_chart_of_accounts_2(asset_name, 100, starting_num)
    make_chart_of_accounts_2(liability_name, 200, starting_num)
    make_chart_of_accounts_2(capital_name, 300, starting_num)
    make_chart_of_accounts_2(drawing_name, 300, starting_num)
    make_chart_of_accounts_2(revenue_name, 400, starting_num)
    make_chart_of_accounts_2(expense_name, 500, starting_num)
    if scroll_down and _bottom > first_line_y-50:
        _top -= 10
        _bottom -= 10
    if scroll_up and _top < HEIGHT:
        _top += 10
        _bottom += 10
    arcadeplus.set_viewport(0, WIDTH, _bottom, _top)
    if save:
        image = arcadeplus.get_image(0, _bottom)
        image.save(f'chart_of_accounts{coa_save_num}.png', 'PNG')
        coa_save_num += 1
        arcadeplus.draw_rectangle_filled(500, 345, 1000, 690, arcadeplus.color.WHITE)


def make_chart_of_accounts_2(acct_t_name, series_num, starting_num):
    global first_line_y, acct_num
    if acct_t_name != drawing_name:
        acct_num = 1
    for n in range(len(acct_t_name)):
        arcadeplus.draw_text(f'{series_num+(acct_num*starting_num)} {acct_t_name[n]}', 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        first_line_y -= 25
        acct_num += 1
        if n == len(acct_t_name) - 1 and acct_t_name != capital_name:
            first_line_y -= 25


def make_trial_balance():
    global total_credits, total_debits, _bottom, _top, first_line_y, tb_save_num
    global tb_name, tb_title, tb_date, tb_col1, tb_col2
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    date = f'{month} {day}, {year}'
    worksheet = 'Trial Balance'
    arcadeplus.draw_text(name, tb_name_x, 660, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(worksheet, tb_title_x, 635, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(date, tb_date_x, 610, arcadeplus.color.BLACK, 16, font_name='calibri')
    first_line_y = 573
    total_debits = 0
    total_credits = 0
    make_trial_balance_2(asset_name, asset_value, asset_cr_dr)
    make_trial_balance_2(liability_name, liability_value, liability_cr_dr)
    make_trial_balance_2(capital_name, capital_value, capital_cr_dr)
    make_trial_balance_2(drawing_name, drawing_value, drawing_cr_dr)
    make_trial_balance_2(revenue_name, revenue_value, revenue_cr_dr)
    make_trial_balance_2(expense_name, expense_value, expense_cr_dr)
    if currency_pos == 'before':
        arcadeplus.draw_text(currency+str(total_debits), c_tb_col1x, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
        arcadeplus.draw_text(currency+str(total_credits), c_tb_col2x, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
    else:
        arcadeplus.draw_text(str(total_debits)+currency, c_tb_col1x, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
        arcadeplus.draw_text(str(total_credits)+currency, c_tb_col2x, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
    if scroll_down and _bottom > first_line_y-50:
        _top -= 10
        _bottom -= 10
    if scroll_up and _top < HEIGHT:
        _top += 10
        _bottom += 10
    arcadeplus.set_viewport(0, WIDTH, _bottom, _top)
    if 660 <= mouse_y <= 680 and mouse_press:
        tb_name = True
        tb_date = False
        tb_title = False
        tb_col1 = False
        tb_col2 = False
    elif 635 <= mouse_y <= 655 and mouse_press:
        tb_title = True
        tb_name = False
        tb_date = False 
        tb_col1 = False
        tb_col2 = False
    elif 610 <= mouse_y <= 630 and mouse_press:
        tb_date = True
        tb_name = False
        tb_title = False
        tb_col1 = False
        tb_col2 = False
    elif 396 <= mouse_x <= 595 and first_line_y-35 <= mouse_y <= 593 and mouse_press:
        tb_col1 = True
        tb_date = False
        tb_name = False
        tb_col2 = False
        tb_title = False
    elif 596 <= mouse_x <= 995 and first_line_y-35 <= mouse_y <= 593 and mouse_press:
        tb_col2 = True
        tb_col1 = False
        tb_date = False
        tb_title = False
        tb_name = False
    elif 0 <= mouse_x <= 395 and first_line_y-35 <= mouse_y <= 593 and mouse_press:
        tb_name = False
        tb_title = False
        tb_date = False
        tb_col1 = False
        tb_col2 = False
    if save:
        tb_name = False
        tb_title = False
        tb_date = False
        tb_col1 = False
        tb_col2 = False
    if tb_name:
        arcadeplus.draw_rectangle_outline(500, 670, 900, 20, arcadeplus.color.BLACK)
    elif tb_title:
        arcadeplus.draw_rectangle_outline(500, 645, 900, 20, arcadeplus.color.BLACK)
    elif tb_date:
        arcadeplus.draw_rectangle_outline(500, 620, 900, 20, arcadeplus.color.BLACK)
    elif tb_col1:
        arcadeplus.draw_lrtb_rectangle_outline(396, 595, 593, first_line_y-35, arcadeplus.color.BLACK)
    elif tb_col2:
        arcadeplus.draw_lrtb_rectangle_outline(596, 995, 593, first_line_y-35, arcadeplus.color.BLACK)
    if tb_name or tb_title or tb_date or tb_col1 or tb_col2:
        arcadeplus.draw_line(500, 690, 500, 0, arcadeplus.color.BLACK)
    if save:
        image = arcadeplus.get_image(0, _bottom)
        image.save(f'trial_balance{tb_save_num}.png', 'PNG')
        tb_save_num += 1
        arcadeplus.draw_rectangle_filled(500, 345, WIDTH, HEIGHT, arcadeplus.color.WHITE)


def make_trial_balance_2(acct_t_name, acct_t_value, acct_t_cr_dr):
    global first_line_y, total_debits, total_credits
    copy_values = acct_t_value.copy()
    debit_count = 0
    credit_count = 0
    for n in range(len(acct_t_name)):
        arcadeplus.draw_text(acct_t_name[n], 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if acct_t_cr_dr[n] == 'dr':
            if debit_count == 0:
                if currency_pos == 'before':
                    copy_values[n] = currency + str(copy_values[n])
                else:
                    copy_values[n] = str(copy_values[n]) + currency
                debit_count += 1
                arcadeplus.draw_text(str(copy_values[n]), c_tb_col1x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            else:
                arcadeplus.draw_text(str(copy_values[n]), tb_col1x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            total_debits += acct_t_value[n]
        else:
            if credit_count == 0:
                if currency_pos == 'before':
                    copy_values[n] = currency + str(copy_values[n])
                else:
                    copy_values[n] = str(copy_values[n]) + currency
                credit_count += 1
                arcadeplus.draw_text(str(copy_values[n]), c_tb_col2x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            else:
                arcadeplus.draw_text(str(copy_values[n]), tb_col2x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            total_credits += acct_t_value[n]
        first_line_y -= 25


def make_income_statement():
    global _bottom, _top, first_line_y, is_name, is_title, is_date, is_col1, is_col2, is_save_num
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    if f_period == 'year':
        date = f'For the year ended {year}'
    else:
        date = f'For the month ended {month} {month_days[month]}, {year}'
    worksheet = 'Income Statement'
    arcadeplus.draw_text(name, is_name_x, 660, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(worksheet, is_title_x, 635, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(date, is_date_x, 610, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Revenue', 10, 573, arcadeplus.color.BLACK, 16, font_name='calibri')
    first_line_y = 536
    rev_value_copy = []
    exp_value_copy = []
    deb_cred_to_pos_neg(rev_value_copy, revenue_value, revenue_cr_dr, -1, 1)
    deb_cred_to_pos_neg(exp_value_copy, expense_value, expense_cr_dr, 1, -1)
    make_income_statement_2(revenue_name, rev_value_copy)
    if len(revenue_name) >= 2:
        arcadeplus.draw_text('Total Revenue', 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if currency_pos == 'before':
            if total_revenue < 0:
                word = '-' + currency + str(total_revenue*-1)
            else:
                word = currency + str(total_revenue)
        else:
            word = str(total_revenue) + currency
        arcadeplus.draw_text(word, c_is_col2x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
    first_line_y -= 50
    arcadeplus.draw_text('Expenses', 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
    first_line_y -= 38
    make_income_statement_2(expense_name, exp_value_copy)
    if len(expense_name) >= 2:
        arcadeplus.draw_text('Total Expenses', 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if currency_pos == 'before':
            if total_expenses < 0:
                word = '-' + currency + str(total_expenses*-1)
            else:
                word = currency + str(total_expenses)
        else:
            word = str(total_expenses) + currency
        arcadeplus.draw_text(word, c_is_col2x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Net Income', 10, first_line_y-50, arcadeplus.color.BLACK, 16, font_name='calibri')
    if currency_pos == 'before':
        if total_revenue - total_expenses < 0:
            net_income = '-' + currency + str((total_revenue-total_expenses)*-1)
        else:
            net_income = currency + str(total_revenue - total_expenses)
    else:
        net_income = str(total_revenue - total_expenses) + currency
    arcadeplus.draw_text(net_income, c_is_col2x, first_line_y-50, arcadeplus.color.BLACK, 16, font_name='calibri')
    if scroll_down and _bottom > first_line_y-50:
        _top -= 10
        _bottom -= 10
    if scroll_up and _top < HEIGHT:
        _top += 10
        _bottom += 10
    arcadeplus.set_viewport(0, WIDTH, _bottom, _top)
    if 660 <= mouse_y <= 680 and mouse_press:
        is_name = True
        is_date = False
        is_title = False
        is_col1 = False
        is_col2 = False
    elif 635 <= mouse_y <= 655 and mouse_press:
        is_title = True
        is_date = False
        is_name = False
        is_col1 = False
        is_col2 = False
    elif 610 <= mouse_y <= 630 and mouse_press:
        is_date = True
        is_title = False
        is_name = False
        is_col1 = False
        is_col2 = False
    elif 396 <= mouse_x <= 595 and first_line_y-35 <= mouse_y <= 593 and mouse_press:
        is_col1 = True
        is_col2 = False
        is_title = False
        is_name = False
        is_date = False
    elif 596 <= mouse_x <= 995 and first_line_y-60 <= mouse_y <= 593 and mouse_press:
        is_col2 = True
        is_col1 = False
        is_title = False
        is_name = False
        is_date = False
    elif 0 <= mouse_x <= 395 and first_line_y-60 <= mouse_y <= 593 and mouse_press:
        is_col2 = False
        is_col1 = False
        is_title = False
        is_name = False
        is_date = False
    if save:
        is_col2 = False
        is_col1 = False
        is_title = False
        is_name = False
        is_date = False
    if is_name:
        arcadeplus.draw_rectangle_outline(500, 670, 900, 20, arcadeplus.color.BLACK)
    elif is_title:
        arcadeplus.draw_rectangle_outline(500, 645, 900, 20, arcadeplus.color.BLACK)
    elif is_date:
        arcadeplus.draw_rectangle_outline(500, 620, 900, 20, arcadeplus.color.BLACK)
    elif is_col1:
        arcadeplus.draw_lrtb_rectangle_outline(396, 595, 593, first_line_y-60, arcadeplus.color.BLACK)
    elif is_col2:
        arcadeplus.draw_lrtb_rectangle_outline(596, 995, 593, first_line_y-60, arcadeplus.color.BLACK)
    if is_name or is_date or is_title or is_col1 or is_col2:
        arcadeplus.draw_line(500, 690, 500, 0, arcadeplus.color.BLACK)
    if save:
        image = arcadeplus.get_image(0, _bottom)
        image.save(f'income_statement{is_save_num}.png', 'PNG')
        is_save_num += 1
        arcadeplus.draw_rectangle_filled(500, 345, WIDTH, HEIGHT, arcadeplus.color.WHITE)


def make_income_statement_2(acct_t_name, copy_list):
    global first_line_y
    for n in range(len(acct_t_name)):
        arcadeplus.draw_text(acct_t_name[n], 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if n == 0:
            if currency_pos == 'before':
                if copy_list[n] < 0:
                    text = '-' + currency + str(copy_list[n]*-1)
                else:
                    text = currency + str(copy_list[n])
            else:
                text = str(copy_list[n]) + currency
            if len(acct_t_name) == 1:
                arcadeplus.draw_text(text, c_is_col2x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            else:
                arcadeplus.draw_text(text, c_is_col1x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        else:
            arcadeplus.draw_text(str(copy_list[n]), is_col1x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        first_line_y -= 25


def deb_cred_to_pos_neg(copy_list, acct_t_value, \
                        acct_t_cr_dr, dr_num, cr_num):
    for n in range(len(acct_t_value)):
        if acct_t_cr_dr[n] == 'dr':
            copy_list.append(acct_t_value[n]*dr_num)
        else:
            copy_list.append(acct_t_value[n]*cr_num)


def entry():
    global asset_name, asset_value, asset_cr_dr, liability_name, liability_value, c_is_col2x, c_is_col1x
    global liability_cr_dr, revenue_name, revenue_value, revenue_cr_dr, expense_name, expense_value
    global expense_cr_dr, capital_name, capital_value, capital_cr_dr, drawing_name, drawing_value
    global drawing_cr_dr, name, month, day, year, f_period, assets, liabilities, capital, drawings
    global revenue, expenses, currency_pos, currency, total_revenue, total_expenses, c_tb_col1x, c_tb_col2x
    home = True
    assets = False
    liabilities = False
    capital = False
    drawings = False
    revenue = False
    expenses = False
    error = False
    total_assets = 0
    total_liabilities = 0
    total_capital = 0
    total_drawings = 0
    total_revenue = 0
    total_expenses = 0
    print("Welcome to Accounting Helper\n")
    print("This app allows you to make a chart of accounts, trial balance, and income statement with a\nsimple input of your assets, liabilities, and owner's equity.\n")
    print("First, type 'assets', 'liabilities', 'capital', 'drawings', 'revenue', or 'expenses' to select the type\nof account that you would like to input.\n")
    print('Please type any names in the following format: lastname;firstname unless otherwise stated\n')
    print("NOTE: PLEASE DO NOT INCLUDE CURRENCY SIGNS when entering the value. You can set the default currency sign by typing 'currency'")
    print("If at any point you want to delete an account, finish entering all the information to the account you are currently entering.\nWhen asked for the next account, type '(del) account name' but replace 'account name' with the account name.")
    print("You can also delete the data of the account that you are in by typing 'empty' when asked to enter the name of your account")
    print('Note: You can only delete an account if that account is part of the menu you are in. For example, you can only\ndelete assets when you are in the assets menu.\n')
    print("Type 'back' to go back to the main menu to enter another type of account.\n")
    print("When all data is entered, go back to the main menu and type 'create' to start creating your worksheets.\n")
    while True:
        if home:
            if not error:
                n = input('Please enter the type of account that you would like to enter: ').lower()
            else:
                n = 'create'
                error = False
            if n == 'assets':
                assets = True
                home = False
            elif n == 'liabilities':
                liabilities = True
                home = False
            elif n == 'capital':
                capital = True
                home = False
            elif n == 'drawings':
                drawings = True
                home = False
            elif n == 'revenue':
                revenue = True
                home = False
            elif n == 'expenses':
                expenses = True
                home = False
            elif n == 'create':
                if total_assets != total_liabilities + total_capital - total_drawings + total_revenue - total_expenses:
                    print('The account values do not satisfy the fundamental accounting equation: assets = liabilities + capital - drawings + revenue - expenses')
                    print(f'Assets: {total_assets}, Liabilities: {total_liabilities}, Capital: {total_capital}')
                    print(f'Drawings: {total_drawings}, Revenue: {total_revenue}, Expenses: {total_expenses}')
                    continue
                else:
                    print("Type 'back' at any point to go back to main menu or if you make a mistake in any of the following inputs.")
                    name = input('Please enter the name of your company: ')
                    if name == 'back':
                        continue
                    date = input('Please enter the date in the following format (mm/dd/yyyy): ')
                    if date == 'back':
                        continue
                    try:
                        month = int(date[:2])
                        day = int(date[3:5])
                        year = int(date[-4:])
                    except:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    if error:
                        continue
                    if len(date) != 10:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    elif month <= 0 or month > 12:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    elif year < 0:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    elif day <= 0:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    else:
                        month = month_list[int(date[:2])-1]
                        if month == 'February':
                            if year % 4 == 0:
                                if day > 29:
                                    print('Not a valid date. Please re-enter information')
                                    error = True
                            else:
                                if day > 28:
                                    print('Not a valid date. Please re-enter information')
                                    error = True
                        elif day > month_days[month]:
                            print('Not a valid date. Please re-enter information')
                            error = True
                    if error:
                        continue
                    f_period = input("Please enter 'year' or 'month' for the fiscal period: ").lower()
                    if f_period == 'back':
                        continue
                    if f_period != 'year' and f_period != 'month':
                        print('Not a valid input. Please re-enter information')
                        error = True
                        continue
                    currency = input('Please enter the currency in which you want to use.\nLeaving this blank defaults to $: ')
                    if currency == 'back':
                        continue
                    elif currency == '':
                        currency = '$'
                    elif currency != '':
                        if len(currency) > 1:
                            print('Not a valid currency. Please re-enter information')
                            error = True
                            continue
                        try:
                            check_currency = int(currency)
                            print('Not a valid currency. Please re-enter information')
                            error = True
                            continue
                        except:
                            pass
                    currency_pos = input("By default, the currency sign goes before the money value?\nEnter 'after' to change this or leave this blank for it to stay the same: ")
                    if currency_pos == 'back':
                        continue
                    elif currency_pos == '':
                        currency_pos = 'before'
                    elif currency_pos != 'before' and currency_pos != 'after':
                        print('Not a valid input. Please re-enter information')
                        error = True
                        continue
                    if currency_pos == 'after':
                        c_tb_col1x = 410
                        c_tb_col2x = 610
                        c_is_col1x = 410
                        c_is_col2x = 610
                    break
            else:
                print('Please enter a valid input')
        elif assets:
            print("Please enter accounts receivable in the form of 'a/r debtor'; replace debtor with the debtor")
            print("Note: If debtor is a person, please enter name in this format: 'lastname;firstname'")
            a_name = input('Please enter the name of your asset: ').lower()
            if '(del)' in a_name:
                delete = a_name.find(')')
                try:
                    index = asset_name.index(a_name[delete+2:])
                except:
                    print('Asset not found. Please re-enter.')
                    continue
                if asset_cr_dr[index] == 'dr':
                    total_assets -= asset_value[index]
                else:
                    total_assets += asset_value[index]
                asset_name.pop(index)
                asset_value.pop(index)
                asset_cr_dr.pop(index)
            elif a_name == 'view':
                print(asset_name)
                print(asset_value)
                print(asset_cr_dr)
                continue
            elif a_name == 'back':
                home = True
                assets = False
            elif a_name == 'empty':
                confirm = input("Type 'confirm' to delete all assets or any other key to cancel: ")
                if confirm == 'confirm':
                    asset_name.clear()
                    asset_value.clear()
                    asset_cr_dr.clear()
                    total_assets = 0
                    print('All assets deleted')
                else:
                    continue
            else:
                try:
                    a_value = float(input('Please enter the value of your asset: '))
                except:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                if a_value < 0:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                a_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if a_cr_dr != 'dr' and a_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                asset_name.append(a_name)
                asset_value.append(a_value)
                asset_cr_dr.append(a_cr_dr)
                if a_cr_dr == 'dr':
                    total_assets += a_value
                else:
                    total_assets -= a_value
            if a_name != 'back':
                print(asset_name)
                print(asset_value)
                print(asset_cr_dr)
        elif liabilities:
            print("Plese enter accounts payable in the form of 'a/p creditor'; replace creditor with the creditor")
            print("Note: If creditor is a person, please enter name in this format: 'lastname;firstname'")
            l_name = input('Please enter the name of your liability: ').lower()
            if '(del)' in l_name:
                delete = l_name.find(')')
                try:
                    index = liability_name.index(l_name[delete+2:])
                except:
                    print('Liability not found. Please re-enter.')
                    continue
                if liability_cr_dr[index] == 'dr':
                    total_liabilities += liability_value[index]
                else:
                    total_liabilities -= liability_value[index]
                liability_name.pop(index)
                liability_value.pop(index)
                liability_cr_dr.pop(index)
            elif l_name == 'view':
                print(liability_name)
                print(liability_value)
                print(liability_cr_dr)
                continue
            elif l_name == 'back':
                home = True
                liabilities = False
            elif l_name == 'empty':
                confirm = input("Type 'confirm' to delete all liabilities or any other key to cancel: ")
                if confirm == 'confirm':
                    liability_name.clear()
                    liability_value.clear()
                    liability_cr_dr.clear()
                    total_liabilities = 0
                    print('All liabilities deleted')
                else:
                    continue
            else:
                try:
                    l_value = float(input('Please enter the value of your liability: '))
                except:
                    print('Value was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                if l_value < 0:
                    print('Value was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                l_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if l_cr_dr != 'dr' and l_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                liability_name.append(l_name)
                liability_value.append(l_value)
                liability_cr_dr.append(l_cr_dr)
                if l_cr_dr == 'dr':
                    total_liabilities -= l_value
                else:
                    total_liabilities += l_value
            if l_name != 'back':    
                print(liability_name)
                print(liability_value)
                print(liability_cr_dr)
        elif capital:
            print("Note: Please enter capital accounts in the following format: 'lastname;firstname, capital' or 'lastname;firstinitial., capital")
            c_name = input('Please enter the name of your capital account: ').lower()
            if '(del)' in c_name:
                delete = c_name.find(')')
                try:
                    index = capital_name.index(c_name[delete+2:])
                except:
                    print('Capital account not found. Please re-enter.')
                    continue
                if capital_cr_dr[index] == 'dr':
                    total_capital += capital_value[index]
                else:
                    total_capital -= capital_value[index]
                capital_name.pop(index)
                capital_value.pop(index)
                capital_cr_dr.pop(index)
            elif c_name == 'view':
                print(capital_name)
                print(capital_value)
                print(capital_cr_dr)
                continue
            elif c_name == 'back':
                home = True
                capital = False
            elif c_name == 'empty':
                confirm = input("Type 'confirm' to delete all capital accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    capital_name.clear()
                    capital_value.clear()
                    capital_cr_dr.clear()
                    total_capital = 0
                    print('All capital accounts deleted')
                else:
                    continue
            elif 'capital' not in c_name or ',' not in c_name or ';' not in c_name:
                print('Invalid capital account. Please re-enter')
                continue
            else:
                try:
                    c_value = float(input('Please enter the amount of capital for this account: '))
                except:
                    print('Value was invalid. Terminated previously entered capital account. Please re-enter.')
                    continue
                if c_value < 0:
                    print('Value was invalid. Terminated previously entered capital account. Please re-enter.')
                    continue
                c_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if c_cr_dr != 'dr' and c_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered capital account. Please re-enter.')
                    continue
                capital_name.append(c_name)
                capital_value.append(c_value)
                capital_cr_dr.append(c_cr_dr)
                if c_cr_dr == 'dr':
                    total_capital -= c_value
                else:
                    total_capital += c_value
            if c_name != 'back':
                print(capital_name)
                print(capital_value)
                print(capital_cr_dr)
        elif drawings:
            print("Note: Please enter drawings accounts in the following format: 'lastname;firstname, drawings' or 'lastname;firstname, drawings")
            d_name = input('Please enter the name of your drawings account: ').lower()
            if '(del)' in d_name:
                delete = d_name.find(')')
                try:
                    index = drawing_name.index(d_name[delete+2:])
                except:
                    print('Drawings account not found. Please re-enter.')
                    continue
                if drawing_cr_dr[index] == 'dr':
                    total_drawings -= drawing_value[index]
                else:
                    total_drawings += drawing_value[index]
                drawing_name.pop(index)
                drawing_value.pop(index)
                drawing_cr_dr.pop(index)
            elif d_name == 'view':
                print(drawing_name)
                print(drawing_value)
                print(drawing_cr_dr)
                continue
            elif d_name == 'back':
                home = True
                drawings = False
            elif d_name == 'empty':
                confirm = input("Type 'confirm' to delete all drawings accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    drawing_name.clear()
                    drawing_value.clear()
                    drawing_cr_dr.clear()
                    total_drawings = 0
                    print('All drawings accounts deleted')
                else:
                    continue
            elif 'drawings' not in d_name or ',' not in d_name or ';' not in d_name:
                print('Invalid drawings account. Please re-enter.')
                continue
            else:
                try:
                    d_value = float(input('Please enter the amount of drawings for this account: '))
                except:
                    print('Value was invalid. Terminated previously entered drawings account. Please re-enter.')
                    continue
                if d_value < 0:
                    print('Value was invalid. Terminated previously entered drawings account. Please re-enter.')
                    continue
                d_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if d_cr_dr != 'dr' and d_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered drawings account. Please re-enter.')
                    continue
                drawing_name.append(d_name)
                drawing_value.append(d_value)
                drawing_cr_dr.append(d_cr_dr)
                if d_cr_dr == 'dr':
                    total_drawings += d_value
                else:
                    total_drawings -= d_value
            if d_name != 'back':
                print(drawing_name)
                print(drawing_value)
                print(drawing_cr_dr)
        elif revenue:
            r_name = input('Please enter the name of your revenue: ').lower()
            if '(del)' in r_name:
                delete = r_name.find(')')
                try:
                    index = revenue_name.index(r_name[delete+2:])
                except:
                    print('Revenue account not found. Please re-enter.')
                    continue
                if revenue_cr_dr[index] == 'dr':
                    total_revenue += revenue_value[index]
                else:
                    total_revenue -= revenue_value[index]
                revenue_name.pop(index)
                revenue_value.pop(index)
                revenue_cr_dr.pop(index)
            elif r_name == 'view':
                print(revenue_name)
                print(revenue_value)
                print(revenue_cr_dr)
                continue
            elif r_name == 'back':
                home = True
                revenue = False
            elif r_name == 'empty':
                confirm = input("Type 'confirm' to delete all revenue accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    revenue_name.clear()
                    revenue_value.clear()
                    revenue_cr_dr.clear()
                    total_revenue = 0
                    print('All revenue accounts deleted')
                else:
                    continue
            else:
                try:
                    r_value = float(input('Please enter the amount of revenue for this account: '))
                except:
                    print('Value was invalid. Terminated previously entered revenue account. Please re-enter.')
                    continue
                if r_value < 0:
                    print('Value was invalid. Terminated previously entered revenue account. Please re-enter.')
                    continue
                r_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if r_cr_dr != 'dr' and r_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered revenue account. Please re-enter.')
                    continue
                revenue_name.append(r_name)
                revenue_value.append(r_value)
                revenue_cr_dr.append(r_cr_dr)
                if r_cr_dr == 'dr':
                    total_revenue -= r_value
                else:
                    total_revenue += r_value
            if r_name != 'back':
                print(revenue_name)
                print(revenue_value)
                print(revenue_cr_dr)
        elif expenses:
            e_name = input('Please enter the name of your expense: ').lower()
            if '(del)' in e_name:
                delete = e_name.find(')')
                try:
                    index = expense_name.index(e_name[delete+2:])
                except:
                    print('Expense not found. Please re-enter.')
                    continue
                if expense_cr_dr[index] == 'dr':
                    total_expenses -= expense_value[index]
                else:
                    total_expenses += expense_value[index]
                expense_name.pop(index)
                expense_value.pop(index)
                expense_cr_dr.pop(index)
            elif e_name == 'view':
                print(expense_name)
                print(expense_value)
                print(expense_cr_dr)
                continue
            elif e_name == 'back':
                home = True
                expenses = False
            elif e_name == 'empty':
                confirm = input("Type 'confirm' to delete all expenses accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    expense_name.clear()
                    expense_value.clear()
                    expense_cr_dr.clear()
                    total_expenses = 0
                    print('All expense accounts deleted')
                else:
                    continue
            else:
                try:
                    e_value = float(input('Please enter the cost of the expense: '))
                except:
                    print('Value was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                if e_value < 0:
                    print('Value was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                e_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ").lower()
                if e_cr_dr != 'dr' and e_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                expense_name.append(e_name)
                expense_value.append(e_value)
                expense_cr_dr.append(e_cr_dr)
                if e_cr_dr == 'dr':
                    total_expenses += e_value
                else:
                    total_expenses -= e_value
            if e_name != 'back':
                print(expense_name)
                print(expense_value)
                print(expense_cr_dr)


if __name__ == '__main__':
    entry()
    liquidity_assets()
    liquidity_liabilities()
    sort_liquidity_cap_draw(capital_name, capital_value, capital_cr_dr, 'Capital')
    sort_liquidity_cap_draw(drawing_name, drawing_value, drawing_cr_dr, 'Drawings')
    capitalize(revenue_name)
    capitalize(expense_name)
    setup()