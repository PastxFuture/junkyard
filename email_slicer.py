'''
Collect an email address from the user and then find out if the user has a custom domain name or a popular domain name. For example:

Example:
Input: mary.jane@gmail.com
Output: Hey Mary, I see your email is registered with Google. That's cool!.

'''

import re

def get_email():

    while True:
        try:
            email = input("Enter Your Email: ").strip()
            if re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email):
                print('Valid email.')
                break
            else:
                print('Invalid email, please try again.')
                continue
        except Exception as e:
            print(e)

    # index() function searches for the particular element or character within the string and lists it is associated with and return its index number

    # slice out the username
    username = email[:email.index('@')]

    # slice out the domain
    domain = email[email.index('@') + 1:]

    print(f'Welcome, {username}! Your domain is {domain}.')

get_email()