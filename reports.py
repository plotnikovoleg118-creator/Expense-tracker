"""Functions for analyzing expenses."""

from database import cursor
from utils import get_integer


def category_summary() -> None:
    cursor.execute(
        """
        SELECT categories.name,
            SUM(expenses.amount)
        FROM expenses
        JOIN categories
            ON expenses.category_id = categories.id
        GROUP BY categories.name
        """
    )
    summary = cursor.fetchall()
    if not summary:
        print(f'\nNo Expense found.')
        return
    cursor.execute(
        """
        SELECT SUM(amount)
        FROM expenses
        """
    )
    total = cursor.fetchone()[0]

    print('\n==== Expenses by category ====')
    print(f'\nTotal expense: {total:.2f} €')
    print('\nBy category:\n')

    for category, amount in summary:
        percentage = amount / total * 100
        print(f'{category}: {amount:.2f} € ({percentage:.1f}%)')


def largest_expense() -> None:
    cursor.execute(
        """
        SELECT expenses.description,
        categories.name,
        expenses.amount,
        expenses.date
        FROM expenses
        JOIN categories
            on expenses.category_id = categories.id
        ORDER BY expenses.amount DESC
        LIMIT 1
        """
    )
    biggest_expense = cursor.fetchone()
    if not biggest_expense:
        print('\nNo expense found')
        return
    print(f'\n==== Largest expense ====')
    print(f'Description: {biggest_expense[0]}')
    print(f'Category: {biggest_expense[1]}')
    print(f'Amount: {biggest_expense[2]:.2f} €')
    print(f'Date: {biggest_expense[3]}')


def monthly_summary() -> None:
    cursor.execute(
        """
        SELECT
            strftime('%Y-%m', date) AS month,
            SUM(amount) AS total
        FROM expenses
        GROUP BY strftime('%Y-%m', date)
        ORDER BY strftime('%Y-%m', date)
        """
    )
    summary = cursor.fetchall()

    print('\n==== Expenses by month ====')

    if not summary:
        print('\nNo expense found')
        return

    for month, amount in summary:
        print(f'{month}: {amount:.2f} €')


def average_monthly_expense() -> None:
    cursor.execute(
        """
        SELECT AVG(total)
        FROM (
            SELECT
                strftime('%Y-%m', date) AS month,
                SUM(amount) AS total
            FROM expenses
            GROUP BY strftime('%Y-%m', date)
    )
        """
    )
    average = cursor.fetchone()[0]
    print(f'AVerage monthly expense: {average:.2f} €')


def reports() -> None:
    while True:
        print('\n==== Reports ====')
        print('1. Expenses by category')
        print('2. Expenses by month')
        print('3. Average monthly expense')
        print('4. Largest expense')
        print('5. Back')

        choice = get_integer('Choose action:')
        if choice == 1:
            category_summary()

        elif choice == 2:
            monthly_summary()

        elif choice == 3:
            average_monthly_expense()

        elif choice == 4:
            largest_expense()

        elif choice == 5:
            break

        else:
            print('Invalid choice. Try again.')
