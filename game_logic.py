from user_input import get_user_choice

user_choice = get_user_choice()

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'scissors' and computer_choice == 'paper') or (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer win!"