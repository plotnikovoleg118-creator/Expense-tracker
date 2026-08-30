'''
Here I store functions associated with analytics and insights
'''

from database import cursor

def category_summary():

    #summarize by category
    cursor.execute(
        """SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category"""
    )
    summary = cursor.fetchall()

    #summarize total
    cursor.execute(
        """SELECT SUM(amount)
        FROM expenses"""
    )
    total = cursor.fetchone()[0]

    print('\n==== Expenses by category ====')
    print(f'Total expense: {total:.2f} €')
    print('\nBy category:')

    if not summary:
        print('\nNo expense found')
        return

    for category, amount in summary:
        percentage = amount / total * 100
        print(f'{category}: {amount:.2f} € ({percentage:.1f}%)')