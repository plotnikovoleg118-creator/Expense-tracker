"""Functions for analyzing expenses."""

from database import cursor


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
        SELECT strftime('%Y-%m', date),
            SUM(amount)
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