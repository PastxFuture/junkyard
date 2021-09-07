'''
Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output.
'''

def word_count():
    message = input('Enter message here: ')

    new_message = message.split(' ')

    num = len(new_message)

    print(f'You have {num} words in your message')

word_count()