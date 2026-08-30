'''
Main file where magic happens
'''

from database import conn
from expenses import (
    get_date,
    get_float,
    get_integer,
    add_expense,
    view_expenses,
    update_expense,
    delete_expense
)

from reports import category_summary

def menu():

    print('\n===== KULUHALDURI MENÜÜ =====')
    print('1. Add expense')
    print('2. Check expenses')
    print('3. Update expense')
    print('4. Delete expense')
    print('5. Expense summaries')
    print('6. Exit')

while True:
    menu()
    choice = get_integer('Choose action:')
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
        conn.close()
        print('Goodbye!')
        break
    else:
        print('Invalid choice. Try again!')
