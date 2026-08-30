"""
validation functions
"""

from datetime import datetime
#asks date to display it to consumer and adds it to database
def get_date(prompt):

    while True:
        date_input = input(prompt)

        try:
            date = datetime.strptime(date_input, '%d.%m.%Y')
            return date.strftime('%Y-%m-%d')
        except ValueError:
            print('Correct format: dd.mm.YYYY')

#this function makes sure that we input
#integer
def get_integer(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Enter the number!')

#makes sure that input is a float
def get_float(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Enter the number!')
