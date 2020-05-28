import arcadeplus
import keyboard

WIDTH = 1000
HEIGHT = 690

home_page = True
chart_of_accounts = False
trial_balance = False
balance_sheet = False
income_statement = False
entry_complete = False

month_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
#month_days = {31: ['January', 'March', 'May', 'July', 'August', 'October', 'December'], 30: {'April', 'June', 'September', 'November'}}
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']

asset_name = []
asset_value = []
asset_cr_dr = []

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

def setup():
    arcadeplus.open_window(WIDTH, HEIGHT, "Accounting Helper")
    arcadeplus.set_background_color(arcadeplus.color.WHITE)
    arcadeplus.schedule(update, 1/60)

    # Override arcade window methods
    window = arcadeplus.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcadeplus.run()


def update(delta_time):
    pass


def on_draw():
    arcadeplus.start_render()
    # Draw in here...
    # Create parellel lists of x and y values for trees. Use a while loop to loop through both lists.
    # Loop over index
    if home_page:
        home_page()
    elif chart_of_accounts:
        pass
    elif trial_balance:
        pass
    elif income_statement:
        pass
    elif balance_sheet:
        pass


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def home_page():
    arcadeplus.draw_rectangle_filled(WIDTH/2, 360, 200, 40, arcadeplus.color.LIME_GREEN)


def chart_of_accounts():
    pass


def trial_balance():
    pass


def income_statement():
    pass


def balance_sheet():
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
    print("If at any point you want to delete an account, finish entering all the information to the account you are currently entering.\nWhen asked for the next account, type 'del account name' but replace 'account name' with the account name.")
    print('Note: You can only delete an account if that account is part of the menu you are in. For example, you can only\ndelete assets when you are in the assets menu.\n')
    print("Press esc to go back to the main menu to enter another type of account.\n")
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
                name = input('Please enter the name of your company: ')
                date = input('Please enter the date in the following format (mm/dd/yyyy): ')
                try:
                    month = int(date[:2])
                    day = int(date[3:5])
                    year = int(date[-4:])
                except ValueError:
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
                else:
                    print('Not a valid input. Please re-enter information.')
                    error = True
                    continue
                entry_complete = True
                break
            else:
                print('Please enter a valid input')
        elif assets:
            a_name = input('Please enter the name of your asset: ')
            if 'del' in a_name:
                delete = a_name.find('l')
                try:
                    index = asset_name.index(a_name[delete+2:])
                except ValueError:
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
                except ValueError:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                if a_value < 0:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                a_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if a_cr_dr == 'dr' or a_cr_dr == 'cr':
                    pass
                else:
                    print('Input was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                asset_name.append(a_name)
                asset_value.append(a_value)
                asset_cr_dr.append(a_cr_dr)
            if a_name != 'back':
                print(f'Your current assets are {asset_name}')
        elif liabilities:
            l_name = input('Please enter the name of your liability: ')
            if 'del' in l_name:
                delete = l_name.find('l')
                try:
                    index = liability_name.index(l_name[delete+2:])
                except ValueError:
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
                except ValueError:
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
            c_name = input('Please enter the name of your capital account: ')
            if 'del' in c_name:
                delete = c_name.find('l')
                try:
                    index = capital_name.index(c_name[delete+2:])
                except ValueError:
                    print('Capital account not found. Please re-enter.')
                    continue
                capital_name.pop(index)
                capital_value.pop(index)
                capital_cr_dr.pop(index)
            elif c_name == 'back':
                home = True
                capital = False
            else:
                try:
                    c_value = float(input('Please enter the amount of capital for this account: '))
                except ValueError:
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
            d_name = input('Please enter the name of your drawings account: ')
            if 'del' in d_name:
                delete = d_name.find('l')
                try:
                    index = drawing_name.index(d_name[delete+2:])
                except ValueError:
                    print('Drawings account not found. Please re-enter.')
                    continue
                drawing_name.pop(index)
                drawing_value.pop(index)
                drawing_cr_dr.pop(index)
            elif d_name == 'back':
                home = True
                drawings = False
            else:
                try:
                    d_value = float(input('Please enter the amount of drawings for this account: '))
                except ValueError:
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
            r_name = input('Please enter the name of your revenue: ')
            if 'del' in r_name:
                delete = r_name.find('l')
                try:
                    index = revenue_name.index(r_name[delete+2:])
                except ValueError:
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
                except ValueError:
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
            e_name = input('Please enter the name of your expense: ')
            if 'del' in e_name:
                delete = e_name.find('l')
                try:
                    index = expense_name.index(e_name[delete+2:])
                except ValueError:
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
                except ValueError:
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