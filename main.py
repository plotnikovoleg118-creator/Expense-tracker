"""Main Module for expense manager."""

from database import conn
from expenses import (
    add_expense,
    view_expenses,
    update_expense,
    delete_expense,
    get_integer
)
from reports import category_summary, monthly_summary


def menu() -> None:
    print('\n===== MENU =====')
    print('1. Add expense')
    print('2. View expenses')
    print('3. Update expense')
    print('4. Delete expense')
    print('5. Category summary')
    print('6. Monthly summary')
    print('7. Exit')


while True:
    menu()

    choice = get_integer('Choose action: ')

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        update_expense()

    elif choice == 4:
        delete_expense()

    elif choice == 5:
        category_summary()

    elif choice == 6:
        monthly_summary()

    elif choice == 7:
        conn.close()
        print('Goodbye!')
        break

    else:
        print('Invalid choice. Try again!')
