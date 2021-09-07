# guessing game

import random

def guess_number():

    random_number = random.randint(1, 10)
    guess = 0
    tries = 0
    max_tries = 4

    while guess != random_number:
        if tries < max_tries:

            try:
                guess = int(input('Pick a number between 1 and 10: '))
            except ValueError:
                print('You did not enter a valid number, restart to try again.')
                break

            tries += 1
            if guess > random_number:
                print('Too high, guess again.')
            elif guess < random_number:
                print('Too low, guess again..')
            else:
                print(f'You guessed it correctly, the number was {random_number}')
        else:
            print('Too many tries, you fail..')
            break

guess_number()