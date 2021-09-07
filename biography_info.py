'''
Ask a user for their personal information one question at a time. Then check that the information they entered is valid. Finally, print a summary of all the information they entered back to them.
'''

import re
import datetime 
#from datetime import datetime # from module, import class

def personal_info():
    name = input('What is your name? ')
    
    return name

def date_of_bith():
    year = int(input('What is the year you were born? '))
    month = int(input('What is the month you were born? '))
    day = int(input('What is the day you were born? '))

    dt = datetime.datetime(year=year, month=month, day=day)

    today = datetime.date.today()
    dob = today.year - dt.year - ((today.month, today.day) < (dt.month, dt.day))

    return dob

def post_code():
    while True:
        try:
            postcode = input('Enter your postcode: ')
            if re.match('^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}', postcode):
                print('Valid Postcode.')
                break
            else:
                print('Invalid postcode, please try again.')
                continue
        except Exception as e:
            print(e)
    
    return postcode

def info(name, age, postcode):
    print(f'Name: {name}')
    print(f'Age: {age}')
    print(f'Post Code: {postcode}')


if __name__ == '__main__':
    name = personal_info()
    age = date_of_bith()
    postcode = post_code()
    info(name, age, postcode)