import os
import sys


WIDTH = 80
menu = {'appetizers': ['mozarella sticks', 'calamari', 'hummus'],
        'entrees': ['spaghetti', 'prime rib', 'pad thai'],
        'desserts': ['ice cream', 'pie', 'flan'],
        'drinks': ['iced tea', 'coffee', 'soda']
        }
order = {}


def show_greeting():
    """Print a formatted banner.

    input: none
    returns: none
    """
    blurbs = ['', 'Welcome to Snake\'s Cafe', "Please make your selections from the following menu items",
              'Enter \'quit\' at any time to complete your order', '']
    print('*' * WIDTH)
    for blurb in blurbs:
        print(f'*{blurb.center(WIDTH - 2)}*')
    print('*' * WIDTH)
    print()


def show_menu():
    """Iterate over the menu items for display. For each category, call show_menu_items with the category
    data as argument. The categories list exists to maintain order. Could replace menu with an OrderedList at some point.

    input: none
    returns: none
    """
    categories = ['appetizers', 'entrees', 'desserts', 'drinks']
    for category in categories:
        items = menu[category]
        show_menu_items(category, items)


def show_menu_items(category, items):
    """Takes a category name and item list and prints them out.

    input: category (str)
    input: items (list)
    returns: none
    """
    # Print category name
    print(category.title())
    print('-' * len(category))
    for item in items:
        # Print each item in title case
        print(item.title())
    print()


def show_prompt():
    """Display a prompt instructing the user to make selections.

    input: none
    returns: none
    """
    msg = 'Please enter your selections.'
    print('*' * (len(msg) + 4))
    print(f'* {msg} *')
    print('*' * (len(msg) + 4))
    print()


def get_selection():
    """Read the user's input from prompt.

    input: none
    returns: (str) Input read from user input.
    """
    return input('> ')


def check_input(user_input):
    """Add item to menu or quit, depending on input.(

    input: user_input (str) user's input
    returns: (boolean) True if menu item added successfully, else False
    """
    if user_input == 'quit':
        print('Thanks for ordering from Snake\'s Cafe.')
        os._exit(0)
    # Check each category to look for user's input
    for category in menu:
        if user_input in menu[category]:
            try:
                order[user_input] += 1
            except KeyError:
                order[user_input] = 1
            return True
    return False


def show_confirmation(choice):
    """Accept user's choice as string and print a message confirming the order and total quantity.

    input: choice (str) represents item added to user's order previously
    returns: none
    """
    quantity = order[choice]
    subs = [quantity,
            "order" if quantity == 1 else "orders",
            choice.title(),
            "has" if quantity == 1 else "have"
            ]

    print('\n{} {} of {} {} been added to your meal.\n'.format(*subs))


def run():
    """Entry point into this script. Shows greeting, menu, prompts user for input, and continues
    until user quits.

    input: none
    returns: none
    """
    show_greeting()
    show_menu()
    show_prompt()
    while True:
        # Get user's selection
        choice = get_selection().lower()
        # Check validity of user's choice. Will be True or False
        if check_input(choice):
            show_confirmation(choice)
        else:
            print('\nSorry. That\'s not an item on our menu.\n')


if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        os._exit(0)
