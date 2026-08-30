'''
CRUD and validation
'''

from utils import(
    get_date,
    get_float,
    get_integer
)
from categories import(
    get_category
)
from database import cursor, conn

#adds expense to the database
def add_expense():

    description = input('Description:').strip().capitalize()
    category = get_category()

    while True:
        try:
            amount = get_float('Price:')
            if amount <= 0:
                print('Invalid input. Try again!')
            else:
                break
        except ValueError:
            print('Invalid input. Try again!')

    date = get_date('Date:')

    cursor.execute(
        """INSERT INTO expenses (description, category, amount, date)
        VALUES (?, ?, ?, ?)""",
        (description, category, amount, date)
    )
    conn.commit()
    print('Expense saved!')

#displays all expenses stored in database
#displays row number different from ID
def view_expenses():

    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = cursor.fetchall()
    if not expenses:
        print('\nNo expense found')
    else:
        print('\n===== Expenses =====')
        for row_number, expense in enumerate(expenses, start=1):
            print(
                f'Row: {row_number} | '
                f'ID: {expense[0]} | '
                f'Description: {expense[1]} | '
                f'Category: {expense[2]} | '
                f'Total: {expense[3]:.2f} € | '
                f'Date: {expense[4]} |'
            )

def update_expense():

    row_number = get_integer('Enter row number:')
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = cursor.fetchall()

    if row_number < 1 or row_number > len(expenses):
        print('No row found')
        return
    expense_id = expenses[row_number - 1][0]

    new_description = input('Description: ').strip().capitalize()
    new_category = get_category()
    new_amount = get_float('Price:')
    new_date = get_date('Date:')
    cursor.execute(
        """UPDATE expenses
        SET description = ?, category = ?, amount = ?, date = ?
        WHERE id = ?""",
        (new_description, new_category, new_amount, new_date, expense_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print('Expense updated!')
    else:
        print('Row was not found.')

def delete_expense():

    row_number = get_integer('Enter row number:')
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = cursor.fetchall()

    if row_number < 1 or row_number > len(expenses):
        print('Row was not found.')
        return
    expense_id = expenses[row_number - 1][0]
    cursor.execute(
        """DELETE FROM expenses
        WHERE id = ?""",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print('Expense deleted!')
    else:
        print('Something went wrong.')
