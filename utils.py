"""Functions for validating and converting user input."""

from datetime import datetime


def get_date(prompt: str) -> str:
    while True:
        date_input = input(prompt)

        try:
            date = datetime.strptime(date_input, '%d.%m.%Y')
            return date.strftime('%Y-%m-%d')
        except ValueError:
            print('Correct format: dd.mm.YYYY')


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Enter the number!')


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Enter the number!')
