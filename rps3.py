import random
import tools

tie = "It's a tie"
win = "You win"
lose = "You lose"

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

outcomes = [[tie, lose, win, win, lose],
            [win, tie, lose, lose, win],
            [lose, win, tie, win, lose],
            [lose, win, lose, tie, win],
            [win, lose, win, lose, tie]]


def play_one_round():

    user = tools.ask_user_for_int("\nWhat would you like to choose? 1 = Rock, 2 = Paper, 3 = Scissors, 4 = Lizard, 5 = Spock ",1,5)
    # lookup of a 1D list - provide 1 set of brackets and 1 index ---> list[index]
    print('You chose', options[user - 1])

    comp = random.randint(1,5)
    # lookup of a 1D list - provide 1 set of brackets and 1 index ---> list[index]
    print('Computer chose', options[comp - 1])

    # lookup of a 2D list - provide 2 sets of brackets and 2 indexes ---> list[index]
    print(outcomes[user - 1][comp - 1])


def main():
    print("Welcome to Rock Paper Scissors!")

    num_times = tools.ask_user_for_int("How many times would you like to play the game?: ",0,20)
    for x in range(num_times):
        play_one_round()

    print("\nThanks for playing!")


main()