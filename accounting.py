import arcadeplus

WIDTH = 1000
HEIGHT = 690

_left = 0
_right = WIDTH
_bottom = 0
_top = HEIGHT

scroll_down = False
scroll_up = False

home_page = True
chart_of_accounts = False
trial_balance = False
balance_sheet = False
income_statement = False
main_menu = False

home_page_press = False
chart_of_accounts_press = False
trial_balance_press = False
balance_sheet_press = False
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
    arcadeplus.start_render()
    # Draw in here...
    if home_page:
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
    elif balance_sheet:
        pass


def on_key_press(key, modifiers):
    global main_menu, scroll_down, scroll_up, interval_selection_page
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = True
    if not home_page and interval_selection_page:
        if key == arcadeplus.key.DOWN:
            scroll_down = True
        if key == arcadeplus.key.UP:
            scroll_up = True


def on_key_release(key, modifiers):
    global main_menu, home_page, chart_of_accounts
    global trial_balance, income_statement, balance_sheet
    global scroll_up, scroll_down, interval_selection_page
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = False
            home_page = True
            chart_of_accounts = False
            trial_balance = False
            income_statement = False
            balance_sheet = False
    if not home_page and interval_selection_page:
        if key == arcadeplus.key.DOWN:
            scroll_down = False
        if key == arcadeplus.key.UP:
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
    balance_sheet_bttn(WIDTH/2, 250, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    arcadeplus.draw_text('Chart of Accounts', 430, 388, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Trial Balance', 450, 338, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Income Statement', 428, 288, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Balance Sheet', 445, 238, arcadeplus.color.BLACK, 16, font_name='calibri')
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


def balance_sheet_bttn(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global balance_sheet_press, home_page, balance_sheet
    left = centre_x - width/2
    right = centre_x + width/2
    top = centre_y + height/2
    bottom = centre_y - height/2
    if left <= mouse_x <= right and bottom <= mouse_y <= top and mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_press)
        balance_sheet_press = True
    elif left <= mouse_x <= right and bottom <= mouse_y <= top and not mouse_press:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_hover)
        if balance_sheet_press:
            balance_sheet_press = False
            balance_sheet = True
            home_page = False
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        balance_sheet_press = False


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
    global bank, liability_name, liability_value, liability_cr_dr, count
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


def liquidity_capital_drawings():
    global capital_name, capital_value, capital_cr_dr
    global drawing_name, drawing_value, drawing_cr_dr
    sort_liquidity_cap_draw(capital_name, capital_value, capital_cr_dr, 'Capital')
    sort_liquidity_cap_draw(drawing_name, drawing_value, drawing_cr_dr, 'Drawings')


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
    global asset_name, liability_name, capital_name, first_line_y
    global expense_name, revenue_name, drawing_name
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
    global asset_name, asset_value, asset_cr_dr, liability_name, liability_value
    global liability_cr_dr, capital_name, capital_value, capital_cr_dr, drawing_name
    global drawing_value, drawing_cr_dr, revenue_name, revenue_value, revenue_cr_dr
    global expense_name, expense_value, expense_cr_dr, name, month, day, year, first_line_y
    global total_credits, total_debits, currency, currency_pos
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    date = f'{month} {day}, {year}'
    worksheet = 'Trial Balance'
    arcadeplus.draw_text(name, 400, 660, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(worksheet, 400, 635, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(date, 400, 610, arcadeplus.color.BLACK, 16, font_name='calibri')
    first_line_y = 573
    total_debits = 0
    total_credits = 0
    make_trial_balance_2(asset_name, asset_value, asset_cr_dr)
    make_trial_balance_2(liability_name, liability_value, liability_cr_dr)
    make_trial_balance_2(capital_name, capital_value, capital_cr_dr)
    make_trial_balance_2(drawing_name, drawing_value, drawing_cr_dr)
    make_trial_balance_2(revenue_name, revenue_value, revenue_cr_dr)
    make_trial_balance_2(expense_name, expense_value, expense_cr_dr)
    arcadeplus.draw_line(355, first_line_y, 500, first_line_y, arcadeplus.color.BLACK)
    arcadeplus.draw_line(555, first_line_y, 700, first_line_y, arcadeplus.color.BLACK)
    if currency_pos == 'before':
        arcadeplus.draw_text(currency+str(total_debits), 400, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
        arcadeplus.draw_text(currency+str(total_credits), 600, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
    else:
        arcadeplus.draw_text(str(total_debits)+currency, 400, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
        arcadeplus.draw_text(str(total_credits)+currency, 600, first_line_y-25, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_line(355, first_line_y-30, 500, first_line_y-30, arcadeplus.color.BLACK)
    arcadeplus.draw_line(355, first_line_y-35, 500, first_line_y-35, arcadeplus.color.BLACK)
    arcadeplus.draw_line(555, first_line_y-30, 700, first_line_y-30, arcadeplus.color.BLACK)
    arcadeplus.draw_line(555, first_line_y-35, 700, first_line_y-35, arcadeplus.color.BLACK)


def make_trial_balance_2(acct_t_name, acct_t_value, acct_t_cr_dr):
    global first_line_y, currency_pos, currency
    global total_debits, total_credits
    copy_values = acct_t_value.copy()
    debit_count = 0
    credit_count = 0
    for n in range(len(acct_t_name)):
        arcadeplus.draw_text(acct_t_name[n], 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if acct_t_cr_dr[n] == 'dr':
            x = 410
            if debit_count == 0:
                if currency_pos == 'before':
                    copy_values[n] = currency + str(copy_values[n])
                    x = 400
                else:
                    copy_values[n] = str(copy_values[n]) + currency
                debit_count += 1
            arcadeplus.draw_text(str(copy_values[n]), x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            total_debits += acct_t_value[n]
        else:
            x = 610
            if credit_count == 0:
                if currency_pos == 'before':
                    copy_values[n] = currency + str(copy_values[n])
                    x = 600
                else:
                    copy_values[n] = str(copy_values[n]) + currency
                credit_count += 1
            arcadeplus.draw_text(str(copy_values[n]), x, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
            total_credits += acct_t_value[n]
        first_line_y -= 25


def make_income_statement():
    global revenue_name, revenue_cr_dr, revenue_value, name
    global expense_name, expense_value, expense_cr_dr, day
    global year, f_period, currency, currency_pos, month
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    if f_period == 'year':
        date = f'For the year ended {year}'
    else:
        date = f'For the month ended {month} {month_days[month]}, {year}'
    worksheet = 'Income Statement'
    arcadeplus.draw_text(name, 400, 660, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(worksheet, 400, 635, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text(date, 400, 610, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_text('Revenue', 10, 573, arcadeplus.color.BLACK, 16, font_name='calibri')
    arcadeplus.draw_line(5, 573, 85, 573, arcadeplus.color.BLACK)
    first_line_y = 548
    deb_cred_to_pos_neg(revenue_value, revenue_cr_dr, -1, 1)
    deb_cred_to_pos_neg(expense_value, expense_cr_dr, 1, -1)
    for n in range(len(revenue_name)):
        arcadeplus.draw_text(revenue_name[n], 10, first_line_y, arcadeplus.color.BLACK, 16, font_name='calibri')
        if n == 0:
            if len(revenue_name) == 1:
                arcadeplus.draw_text(revenue_value.)


def deb_cred_to_pos_neg(copy_list, acct_t_value, acct_t_cr_dr, dr_num, cr_num):
    copy_list = []
    for n in range(len(acct_t_value)):
        if acct_t_cr_dr[n] == 'dr':
            copy_list.append(acct_t_value[n]*dr_num)
        else:
            copy_list.append(acct_t_value[n]*cr_num)



def make_balance_sheet():
    pass


def entry():
    global asset_name, asset_value, asset_cr_dr, liability_name, liability_value
    global liability_cr_dr, revenue_name, revenue_value, revenue_cr_dr, expense_name, expense_value
    global expense_cr_dr, capital_name, capital_value, capital_cr_dr, drawing_name, drawing_value
    global drawing_cr_dr, name, month, day, year, f_period, assets, liabilities, capital, drawings
    global revenue, expenses, currency_pos, currency
    home = True
    assets = False
    liabilities = False
    capital = False
    drawings = False
    revenue = False
    expenses = False
    error = False
    print("Welcome to Accounting Helper\n")
    print("This app allows you to make a chart of accounts, trial balance, income statement, and balance sheet with a\nsimple input of your assets, liabilities, and owner's equity.\n")
    print("First, type 'assets', 'liabilities', 'capital', 'drawings', 'revenue', or 'expenses' to select the type\nof account that you would like to input.\n")
    print('Please type any names in the following format: lastname;firstname unless otherwise stated\n')
    print("NOTE: PLEASE DO NOT INCLUDE CURRENCY SIGNS when entering the value. You can set the default currency sign by typing 'currency'") #need to add
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
                if len(asset_name) != 0 and len(capital_name) == 0:
                    print('Capital Account is required to start creating worksheets.')
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
                    elif month < 0 or month > 12:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    elif year < 0:
                        print('Not a valid date. Please re-enter information.')
                        error = True
                    elif day < 0:
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
                    if currency != '':
                        try:
                            check_currency = int(currency)
                            if len(currency) > 1:
                                print('Not a valid currency. Please re-enter information')
                                error = True
                                continue
                        except:
                            pass
                    currency_pos = input("Does the currency go before or after the money value?\nEnter 'before' or 'after'. Leaving this blank defaults to before: ")
                    if currency_pos == 'back':
                        continue
                    if currency_pos != 'before' and currency_pos != 'after' and currency_pos != '':
                        print('Not a valid input. Please re-enter information')
                        error = True
                        continue
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
                asset_name.pop(index)
                asset_value.pop(index)
                asset_cr_dr.pop(index)
            elif a_name == 'back':
                home = True
                assets = False
            elif a_name == 'empty':
                confirm = input("Type 'confirm' to delete all assets or any other key to cancel: ")
                if confirm == 'confirm':
                    asset_name.clear()
                    asset_value.clear()
                    asset_cr_dr.clear()
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
            if a_name != 'back':
                print(f'Your current assets are {asset_name}')
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
                liability_name.pop(index)
                liability_value.pop(index)
                liability_cr_dr.pop(index)
            elif l_name == 'back':
                home = True
                liabilities = False
            elif l_name == 'empty':
                confirm = input("Type 'confirm' to delete all liabilities or any other key to cancel: ")
                if confirm == 'confirm':
                    liability_name.clear()
                    liability_value.clear()
                    liability_cr_dr.clear()
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
            if l_name != 'back':    
                print(f'Your current liabilities are {liability_name}')
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
                capital_name.pop(index)
                capital_value.pop(index)
                capital_cr_dr.pop(index)
            elif c_name == 'back':
                home = True
                capital = False
            elif c_name == 'empty':
                confirm = input("Type 'confirm' to delete all capital accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    capital_name.clear()
                    capital_value.clear()
                    capital_cr_dr.clear()
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
            if c_name != 'back':
                print(f'Your current capital accounts are {capital_name}')
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
                drawing_name.pop(index)
                drawing_value.pop(index)
                drawing_cr_dr.pop(index)
            elif d_name == 'back':
                home = True
                drawings = False
            elif d_name == 'empty':
                confirm = input("Type 'confirm' to delete all drawings accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    drawing_name.clear()
                    drawing_value.clear()
                    drawing_cr_dr.clear()
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
            if d_name != 'back':
                print(f'Your current drawings accounts are {drawing_name}')
        elif revenue:
            r_name = input('Please enter the name of your revenue: ').lower()
            if '(del)' in r_name:
                delete = r_name.find(')')
                try:
                    index = revenue_name.index(r_name[delete+2:])
                except:
                    print('Revenue account not found. Please re-enter.')
                    continue
                revenue_name.pop(index)
                revenue_value.pop(index)
                revenue_cr_dr.pop(index)
            elif r_name == 'back':
                home = True
                revenue = False
            elif r_name == 'empty':
                confirm = input("Type 'confirm' to delete all revenue accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    revenue_name.clear()
                    revenue_value.clear()
                    revenue_cr_dr.clear()
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
            if r_name != 'back':
                print(f'Your current revenue accounts are {revenue_name}')
        elif expenses:
            e_name = input('Please enter the name of your expense: ').lower()
            if '(del)' in e_name:
                delete = e_name.find(')')
                try:
                    index = expense_name.index(e_name[delete+2:])
                except:
                    print('Expense not found. Please re-enter.')
                    continue
                expense_name.pop(index)
                expense_value.pop(index)
                expense_cr_dr.pop(index)
            elif e_name == 'back':
                home = True
                expenses = False
            elif e_name == 'empty':
                confirm = input("Type 'confirm' to delete all expenses accounts or any other key to cancel: ")
                if confirm == 'confirm':
                    expense_name.clear()
                    expense_value.clear()
                    expense_cr_dr.clear()
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
            if e_name != 'back':
                print(f'Your current expenses are {expense_name}')


if __name__ == '__main__':
    entry()
    liquidity_assets()
    liquidity_liabilities()
    liquidity_capital_drawings()
    capitalize(revenue_name)
    capitalize(expense_name)
    setup()