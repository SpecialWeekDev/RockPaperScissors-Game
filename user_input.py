def get_user_choice():

    OPTIONS = ['rock', 'paper', 'scissors']

    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if choice in OPTIONS:
            return choice
        else:
            print("Invalid choice. Please try again.")