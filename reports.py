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

    #summarize total
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

    if not summary:
        print('\nNo expense found')
        return

    for category, amount in summary:
        percentage = amount / total * 100
        print(f'{category}: {amount:.2f} € ({percentage:.1f}%)')

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
        print(f'{month}: {amount: .2f} €')

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
        print('4. Back')

        choice = get_integer('Choose action:')
        if choice == 1:
            category_summary()

        elif choice == 2:
            monthly_summary()

        elif choice == 3:
            average_monthly_expense()

        elif choice == 4:
            break
        else:
            print('Invalid choice. Try again.')
