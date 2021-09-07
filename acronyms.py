'''
Ask the user to enter the full meaning of an organization or concept and you'll provide the acronym to the user. For example:
'''

def acronym():
    phrase = input('Please enter a full meaning of a concept / organisaition: ')

    list_phrase = phrase.split(' ')
    the_acronym = ''

    for each_word in list_phrase:
        the_acronym += each_word[0]
    
    return the_acronym.upper()

print(acronym())