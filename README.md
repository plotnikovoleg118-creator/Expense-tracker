# Expense Tracker

A simple command-line expense tracking application built with Python and SQLite.

## Features

* Add expenses
* View expenses
* Update expenses
* Delete expenses
* Add and manage categories
* Validate user input
* Store expense dates
* Generate expense summaries by category
* Generate expense summaries by month

## Technologies

* Python
* SQLite

## Project Structure

```text
expense-tracker/
├── main.py
├── database.py
├── expenses.py
├── categories.py
├── reports.py
├── utils.py
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.
2. Open the project folder in VS Code.
3. Run:

```bash
python main.py
```

The SQLite database is created automatically when the application starts.

## Current Version

**v0.3**

This project is currently under development. The current version includes normalized category data, SQL JOIN queries, and basic expense analysis by category and month.
