''''
Ask the user for an input.
This could be anything such as a name, an adjective, a pronoun or even an action. Once you get the input, you can rearrange it to build up your own story.
'''

def mad_libs():
    name = input('Pick a name: ')
    city = input('Pick a city: ')
    animal = input('Pick an animal: ')
    action = input('Pick an action: ')
    colour = input('Pick a colour: ')
    element = input('Pick an element: ')

    return name, city, animal, action, colour, element

def script(name, city, animal, action, colour, element):
    print(f'''
    My name is {name} and I am from {city}. My favourite animal is a {animal} because they {action}. My favourite colour is {colour} and out of the 4 elements, my favourite is {element}.
    ''')

name, city, animal, action, colour, element = mad_libs()
script(name, city, animal, action, colour, element)