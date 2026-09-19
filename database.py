'''
SQL code and stuff related to database
'''

import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / 'expenses.db'
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE
                )
                ''')

default_categories = [
    'Food',
    'Transportation',
    'Entertainment',
    'Living expenses',
    'Other'
]

for category in default_categories:
    cursor.execute(
        'INSERT OR IGNORE INTO categories (name) VALUES (?)',
        (category,)
    )

cursor.execute('''
               CREATE TABLE IF NOT EXISTS expenses (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT NOT NULL,
                   category_id INTEGER NOT NULL REFERENCES categories(id),
                   amount REAL NOT NULL,
                   date TEXT NOT NULL
               )
               ''')

#cursor.execute('DELETE FROM categories WHERE name = ?', ('Tervis',))
conn.commit()
