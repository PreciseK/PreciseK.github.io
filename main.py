import random


def is_win(player, opponent):
    if (player == 'P' and opponent == 'R') or (player == 'R' and opponent == 'S') \
            or (player == 'S' and opponent == 'P'):
        return True


def play():
    user = input("What's your choice? 'R' for rock, 'S' for scissors and 'P' for paper:\n").upper()
    computer = random.choice(['R', 'S', 'P'])
    print(user)
    if user == 'R' or 'S' or 'P':
        if is_win(user, computer):
            return 'You Won!!!'
        elif user == computer:
            return "It's a tie"
        else:
            return 'You lost!!!'
    else:
        return 'You have entered the wrong input, restart game.'


print(play())
