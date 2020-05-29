import arcadeplus

WIDTH = 1000
HEIGHT = 690

home_page = True
chart_of_accounts = False
trial_balance = False
balance_sheet = False
income_statement = False
entry_complete = False
main_menu = False

home_page_press = False
chart_of_accounts_press = False
trial_balance_press = False
balance_sheet_press = False
income_statement_press = False

interval5 = False
interval1 = False
interval_selection_done = False

month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
#month_days = {31: ['January', 'March', 'May', 'July', 'August', 'October', 'December'], 30: {'April', 'June', 'September', 'November'}}
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

asset_name = []
asset_value = []
asset_cr_dr = []

a_r_name = []
a_r_value = []
a_r_dc = []
a_r_value_dc = []
a_r_dict = {}
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

    arcadeplus.run()


def update(delta_time):
    pass


def on_draw():
    global home_page, chart_of_accounts, trial_balance, income_statement
    global main_menu, balance_sheet, interval_selection_done
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
        pass
    elif income_statement:
        pass
    elif balance_sheet:
        pass
    if main_menu:
        home_page = True
        interval_selection_done = False
        chart_of_accounts = False
        trial_balance = False
        income_statement = False
        balance_sheet = False


def on_key_press(key, modifiers):
    global main_menu, home_page
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = True


def on_key_release(key, modifiers):
    global main_menu, home_page
    if not home_page:
        if key == arcadeplus.key.ESCAPE:
            main_menu = False


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
    global chart_of_accounts_press, home_page, chart_of_accounts
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
    arcadeplus.set_background_color(arcadeplus.color.DARK_BLUE_GRAY)
    arcadeplus.draw_text('Select the interval in which you want your account numbers to go up by.', 70, 530, arcadeplus.color.WHITE, 24, font_name='calibri')
    account_interval1(WIDTH/2, 390, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    account_interval5(WIDTH/2, 300, 200, 40, arcadeplus.color.WHITE, arcadeplus.color.GREEN_YELLOW, arcadeplus.color.LIME_GREEN)
    arcadeplus.draw_text('1s', 488, 379, arcadeplus.color.WHITE, 16, font_name='calibri')
    arcadeplus.draw_text('5s', 488, 289, arcadeplus.color.WHITE, 16, font_name='calibri')


def account_interval5(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global interval5, interval_selection_done
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
        else:
            arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
            interval_selection_done = False
            interval5 = False


def account_interval1(centre_x, centre_y, width, height, color_press, color_hover, color_default):
    global interval1, interval_selection_done
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
    else:
        arcadeplus.draw_rectangle_filled(centre_x, centre_y, width, height, color_default)
        interval_selection_done = False
        interval1 = False


def liquidity():
    global asset_name, asset_value, asset_cr_dr, a_r_dict, a_r_name, a_r_value, bank
    global a_r_dc, a_r_value_dc
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
    n_assets = len(asset_name)
    for n in range(n_assets):
        if 'accounts receivable' in asset_name[n]:
            a_r = asset_name[n]
            reverse = a_r[::-1]
            i = reverse.find('elbaviecer stnuocca')
        elif 'a/r' in asset_name[n]:
            a_r = asset_name[n]
            reverse = a_r[::-1]
            i = reverse.find('r/a')
        if 'accounts receivable' in asset_name[n] or 'a/r' in asset_name[n]:
            r_debtor = reverse[:i]
            debtor = r_debtor[::-1]
            comma = debtor.find(',')
            if comma == -1:
                a_r_name.append(debtor)
            else:
                debtor_name = debtor[comma+1:] + debtor[:comma]
                a_r_name.append(debtor_name)
            asset_name.remove(asset_name[n])
            a_r_value.append(asset_value[n])
            a_r_dc.append(asset_cr_dr[n])
            asset_value.pop(n)
            asset_cr_dr.pop(n)
    if len(a_r_name) != 0:
        for n in range(len(a_r_name)):
            a_r_value_dc.append([a_r_value[n], a_r_dc[n]])
        for n in a_r_name:
            for x, y in a_r_value_dc:
                a_r_value_dc[n] = x, y
                a_r_value_dc.remove([x, y])
                break
        alphabetical_a_r = sorted(a_r_value_dc)
        a_r_value.clear()
        a_r_dc.clear()
        for n in alphabetical_a_r:
            a_r_value.append(a_r_value_dc[n][0])
            a_r_dc.append(a_r_value_dc[n][1])
        #add name, values, and dr_cr back to respective asset lists


def make_chart_of_accounts():
    arcadeplus.set_background_color(arcadeplus.color.WHITE)


def make_trial_balance():
    pass


def make_income_statement():
    pass


def make_balance_sheet():
    pass


def entry():
    global entry_complete, asset_name, asset_value, asset_cr_dr, liability_name, liability_value
    global liability_cr_dr, revenue_name, revenue_value, revenue_cr_dr, expense_name, expense_value
    global expense_cr_dr, capital_name, capital_value, capital_cr_dr, drawing_name, drawing_value
    global drawing_cr_dr, name, month, day, year, f_period, month_days, month_list
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
    print('Please type any names in the following format: lastname, firstname')
    print("If at any point you want to delete an account, finish entering all the information to the account you are currently entering.\nWhen asked for the next account, type '(del) account name' but replace 'account name' with the account name.")
    print('Note: You can only delete an account if that account is part of the menu you are in. For example, you can only\ndelete assets when you are in the assets menu.\n')
    print("Type 'back' to go back to the main menu to enter another type of account.\n")
    print("When all data is entered, go back to the main menu and type 'create' to start creating your worksheets.\n")
    while True:
        if home:
            if not error:
                n = input('Please enter the type of account that you would like to enter: ')
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
                f_period = input("Please enter 'year' or 'month' for the fiscal period: ")
                if f_period == 'year' or f_period == 'month':
                    pass
                elif f_period == 'back':
                    continue
                else:
                    print('Not a valid input. Please re-enter information.')
                    error = True
                    continue
                entry_complete = True
                break
            else:
                print('Please enter a valid input')
        elif assets:
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
            else:
                try:
                    a_value = float(input('Please enter the value of your asset: '))
                except:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                if a_value < 0:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                a_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if a_cr_dr != 'dr' and a_cr_dr != 'cr':
                    print('Input was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                asset_name.append(a_name)
                asset_value.append(a_value)
                asset_cr_dr.append(a_cr_dr)
            if a_name != 'back':
                print(f'Your current assets are {asset_name}')
        elif liabilities:
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
            else:
                try:
                    l_value = float(input('Please enter the value of your liability: '))
                except:
                    print('Value was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                if l_value < 0:
                    print('Value was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                l_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if l_cr_dr == 'dr' or l_cr_dr == 'cr':
                    pass
                else:
                    print('Input was invalid. Terminated previously entered liability. Please re-enter.')
                    continue
                liability_name.append(l_name)
                liability_value.append(l_value)
                liability_cr_dr.append(l_cr_dr)
            if l_name != 'back':    
                print(f'Your current liabilities are {liability_name}')
        elif capital:
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
            elif 'capital' not in c_name:
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
                c_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if c_cr_dr == 'dr' or c_cr_dr == 'cr':
                    pass
                else:
                    print('Input was invalid. Terminated previously entered capital account. Please re-enter.')
                    continue
                capital_name.append(c_name)
                capital_value.append(c_value)
                capital_cr_dr.append(c_cr_dr)
            if c_name != 'back':
                print(f'Your current capital accounts are {capital_name}')
        elif drawings:
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
            elif 'drawings' not in d_name:
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
                d_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if d_cr_dr == 'dr' or d_cr_dr == 'cr':
                    pass
                else:
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
            else:
                try:
                    r_value = float(input('Please enter the amount of revenue for this account: '))
                except:
                    print('Value was invalid. Terminated previously entered revenue account. Please re-enter.')
                    continue
                if r_value < 0:
                    print('Value was invalid. Terminated previously entered revenue account. Please re-enter.')
                    continue
                r_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if r_cr_dr == 'dr' or r_cr_dr == 'cr':
                    pass
                else:
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
            else:
                try:
                    e_value = float(input('Please enter the cost of the expense: '))
                except:
                    print('Value was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                if e_value < 0:
                    print('Value was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                e_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if e_cr_dr == 'dr' or e_cr_dr == 'cr':
                    pass
                else:
                    print('Input was invalid. Terminated previously entered expense. Please re-enter.')
                    continue
                expense_name.append(e_name)
                expense_value.append(e_value)
                expense_cr_dr.append(e_cr_dr)
            if e_name != 'back':
                print(f'Your current expenses are {expense_name}')


if __name__ == '__main__':
    entry()
    if entry_complete:
        setup()