"""
Here you can find category-related functions
"""
from database import conn, cursor
from utils import (
    get_integer
)

#this function lets user to add category
def add_category():

    category = input('New category:').strip().capitalize()
    cursor.execute("""INSERT INTO categories (name) VALUES (?)""",
                   (category,))
    conn.commit()

#this function makes category input easier
def get_category():

    while True:
        cursor.execute('SELECT * FROM categories')
        categories = cursor.fetchall()

        for number, category in enumerate(categories, start=1):
            print(f'{number}. {category[1]}')

        print(f'{len(categories) + 1}. Other')
        print(f'{len(categories) + 2}. Add category')

        choice = get_integer('Choose category:')
        if 1 <= choice <= len(categories):
            return categories[choice - 1][1]
        elif choice == len(categories) + 1:
            return 'Muu'
        elif choice == len(categories) + 2:
            add_category()
            return get_category()
        else:
            print('Category was not found.')