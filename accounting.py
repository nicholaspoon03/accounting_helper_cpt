import arcade

WIDTH = 1000
HEIGHT = 690

home_page = True
chart_of_accounts = False
trial_balance = False
balance_sheet = False
income_statement = False

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Accounting Helper")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    # Create parellel lists of x and y values for trees. Use a while loop to loop through both lists.
    # Loop over index
    if home_page:
        pass
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
    arcade.draw_rectangle_filled(WIDTH/2, LENGTH/2, )


def chart_of_accounts():
    pass


def trial_balance():
    pass


def income_statement():
    pass


def balance_sheet():
    pass


if __name__ == '__main__':
    setup()