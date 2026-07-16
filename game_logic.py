import random

OPTIONS = ['rock', 'paper', 'scissors']


def get_computer_choice():
    return random.choice(OPTIONS)

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if choice in OPTIONS:
            return choice
        else:
            print("Invalid choice. Please try again.")

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer win!"
    
def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    player_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = check_winner(player_choice, computer_choice)
    
    print(result)