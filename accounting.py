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

asset_name = []
asset_value = []
asset_cr_dr = []

liability_name = []
liability_value = []
liability_cr_dr = []

revenue_name = []
revenue_value = []
revenue_cr_dr = []

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
    global liability_cr_dr, revenue_name, revenue_value, revenue_cr_dr
    home = True
    assets = False
    liabilities = False
    capital = False
    drawings = False
    revenue = False
    expenses = False
    print("Welcome to Accounting Helper\n")
    print("This app allows you to make a chart of accounts, trial balance, income statement, and balance sheet with a\nsimple input of your assets, liabilities, and owner's equity.\n")
    print("First, type 'assets', 'liabilities', 'capital', 'drawings', 'revenue', or 'expenses' to select the type\nof account that you would like to input.\n")
    print("If at any point you want to delete an account, finish entering all the information to the account you are currently entering.\nWhen asked for the next account, type 'del account name' but replace 'account name' with the account name.")
    print('Note: You can only delete an account if that account is part of the menu you are in. For example, you can only delete assets when you are in the assets menu.\n')
    print("Press esc to go back to the main menu to enter another type of account.\n")
    print("When all data is entered, go back to the main menu and type 'create' to start creating your worksheets.\n")
    while True:
        if home:
            n = input('Please enter the type of account that you would like to enter: ')
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
                entry_complete = True
                break
            else:
                print('Please enter a valid input')
        elif assets:
            a_name = input('Please enter the name of your asset: ')
            if 'del' in a_name:
                delete = a_name.find('l')
                index = asset_name.index(a_name[delete+2:])
                asset_name.pop(index)
                asset_value.pop(index)
                asset_cr_dr.pop(index)
            else:
                try:
                    a_value = float(input('Please enter the value of your asset: '))
                except ValueError:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                if a_value < 0:
                    print('Value was invalid. Terminated previously entered asset. Please re-enter.')
                a_cr_dr = input("Please enter 'dr' for a debit balance or 'cr' for a credit balance: ")
                if a_cr_dr == 'dr' or a_cr_dr == 'cr':
                    pass
                else:
                    print('Input was invalid. Terminated previously entered asset. Please re-enter.')
                    continue
                asset_name.append(a_name)
                asset_value.append(a_value)
                asset_cr_dr.append(a_cr_dr)
        elif liabilities:
            l_name = input('Please enter the name of your liability: ')
            if 'del' in l_name:
                delete = l_name.find('l')
                index = liability_name.index(l_name[delete+2:])
                liability_name.pop(index)
                liability_value.pop(index)
                liability_cr_dr.pop(index)
            else:
                try:
                    l_value = float(input('Please enter the value of your liability: '))
                except ValueError:
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
        elif capital:
            pass
        elif drawings:
            pass
        elif revenue:
            l_name = input('Please enter the name of your liability: ')
            if 'del' in l_name:
                delete = l_name.find('l')
                index = liability_name.index(l_name[delete+2:])
                liability_name.pop(index)
                liability_value.pop(index)
                liability_cr_dr.pop(index)
            else:
                try:
                    l_value = float(input('Please enter the value of your liability: '))
                except ValueError:
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
            print(liability_name)
            print(liability_value)
            print(liability_cr_dr)
        elif expenses:
            pass
       # if Key.esc:
            home = True
            assets = False
            liabilities = False
            capital = False
            drawings = False
            revenue = False
            expenses = False


if __name__ == '__main__':
    entry()
    if entry_complete:
        setup()