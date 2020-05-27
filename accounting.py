import arcadeplus

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
    global entry_complete, asset_name, asset_value, asset_cr_dr
    home = True
    assets = False
    liabilities = False
    capital = False
    drawings = False
    revenue = False
    expenses = False
    print("Welcome to Accounting Helper")
    print("This app allows you to make a chart of accounts, trial balance, income statement, and balance sheet with a\nsimple input of your assets, liabilities, and owner's equity")
    print("First, type 'assets', 'liabilities', 'capital', 'drawings', 'revenue', or 'expenses' to select the type\nof account that you would like to input")
    print("Press esc to go back to the main menu to enter another type of account.")
    print("When all input is create, go back to the main menu and type 'create' to start creating your worksheets.")
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
            elif n == 'expenses'
                expenses = True
                home = False
            elif n == 'create':
                entry_complete = True
            else:
                print('Please enter a valid input')
        elif assets:
            print('If at any point you make a mistake, ')
            name = input('Please enter the name of your asset: ')
        elif liabilities:
            pass
        elif capital:
            pass
        elif drawings:
            pass
        elif revenue:
            pass
        elif expenses:
            pass

if __name__ == '__main__':
    entry()
    if entry_complete:
        setup()