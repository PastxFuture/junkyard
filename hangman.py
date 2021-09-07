# hangman
from words import words
import random
import string

def clean_list(new_list):
    new_list = [x.replace('-', '') for x in words]

    word = random.choice(new_list) # randomly chooses something from the list
    
    return word

def hangman():
    word = clean_list(new_list)
    word_letters = set(word) # letters in teh word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    # get user input
    user_letter = input('Guess a letter: ').upper()


user_input = input('Type something')
print(user_input)
