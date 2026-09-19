"""Category-related functions."""

from database import conn, cursor
from utils import get_integer


def add_category() -> None:
    category = input('New category: ').strip().capitalize()
    cursor.execute("INSERT INTO categories (name) VALUES (?)",
                   (category,)
)
    conn.commit()


def get_category() -> int:
    while True:
        cursor.execute(
            'SELECT * FROM categories WHERE name != ?',
        ('Other',)
        )
        categories = cursor.fetchall()

        cursor.execute(
            'SELECT * FROM categories WHERE name = ?',
            ('Other',)
        )
        other = cursor.fetchone()

        for number, category in enumerate(categories, start=1):
            print(f'{number}. {category[1]}')

        print(f'{len(categories) + 1}. Other')
        print(f'{len(categories) + 2}. Add category')

        choice = get_integer('Choose category: ')
        if 1 <= choice <= len(categories):
            return categories[choice - 1][0]

        elif choice == len(categories) + 1:
            return other[0]

        elif choice == len(categories) + 2:
            add_category()

        else:
            print('Category was not found.')
