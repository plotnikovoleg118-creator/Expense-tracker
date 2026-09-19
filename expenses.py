"""CRUD and validation."""

from utils import (
    get_date,
    get_float,
    get_integer
)
from categories import get_category
from database import cursor, conn


def add_expense() -> None:
    description = input('Description: ').strip().capitalize()
    category_id = get_category()

    while True:
        try:
            amount = get_float('Price: ')
            if amount <= 0:
                print('Invalid input. Try again!')
            else:
                break
        except ValueError:
            print('Invalid input. Try again!')

    date = get_date('Date: ')

    cursor.execute(
        """
        INSERT INTO expenses (description, category_id, amount, date)
        VALUES (?, ?, ?, ?)
        """,
        (description, category_id, amount, date)
    )
    conn.commit()
    print('Expense saved!')


def view_expenses() -> None:
    cursor.execute(
        """
        SELECT expenses.id,
            expenses.description,
            categories.name,
            expenses.amount,
            expenses.date
        FROM expenses
        JOIN categories
            ON expenses.category_id = categories.id
        ORDER BY expenses.date DESC
        """
    )
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


def update_expense() -> None:
    row_number = get_integer('Enter row number: ')
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = cursor.fetchall()

    if row_number < 1 or row_number > len(expenses):
        print('No row found')
        return
    expense_id = expenses[row_number - 1][0]

    new_description = input('Description: ').strip().capitalize()
    new_category_id = get_category()
    new_amount = get_float('Price: ')
    new_date = get_date('Date: ')
    cursor.execute(
        """
        UPDATE expenses
        SET description = ?, category_id = ?, amount = ?, date = ?
        WHERE id = ?
        """,
        (new_description, new_category_id, new_amount, new_date, expense_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print('Expense updated!')
    else:
        print('Row was not found.')


def delete_expense() -> None:
    row_number = get_integer('Enter row number: ')
    cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
    expenses = cursor.fetchall()

    if row_number < 1 or row_number > len(expenses):
        print('Row was not found.')
        return
    expense_id = expenses[row_number - 1][0]
    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        """,
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print('Expense deleted!')
    else:
        print('Something went wrong.')
