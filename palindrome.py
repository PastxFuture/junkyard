'''
Ask the user to give you five words. Then check if any of the five words is a palindrome.

NOTE: A palindrome is a word that remains the same whether it's read forward or backward.
'''

def palin():
    first = input('Enter a word: ')

    if first == first[::-1]:
        print(f'{first} is a palindrome!')
    else:
        print(f'{first} is not a palindrome!')

palin()