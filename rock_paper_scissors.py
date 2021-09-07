# rock paper scissors
import random

def play():
    #r > s, s > p, p > r
    user = input('What is your choice: "r" for rock, "p" for paper, "s" for scissors: ')
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie.'
    
    if is_win(user, computer):
        return 'You won!'


    return 'You lost!'

def is_win(player, oponent):
    #return true if player wins

    if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') or (player == 'p' and oponent == 'r'):
        return True

print(play())