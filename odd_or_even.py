'''
Welcome a user then ask them for a number between 1 and 1000.
When the user gives you the number, you check if it's odd or even and then you print a message letting them know.
'''

def odd_or_even():
    name = input('What is your name? ')
    print(f'Welcome, {name}!')
    
    number = int(input('Pick a number between 1 and 1000: '))

    if (number % 2) == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd.')

odd_or_even()