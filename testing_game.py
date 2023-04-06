import random


# This functions defines if the user is giving a valid input

def is_valid_input(move, choices):
    if move in choices:
        return True
    else:
        return False


# Main Menu
# In the Main Menu we will receive users name. We are creating a list of choices from which the user and the computer
# will be choosing. Afterwards the user will have two possible options for game modes.

# Main Menu
player_name = input("Enter your name:")
computer = "Computer"
print(f"Welcome {player_name}")
choices = ["rock", "paper", "scissors"]

while True:
    answer = input("Do you want to play a game? (Yes/No)")
    if answer.lower() == "no":
        print("Okay, bye!")
        exit()
    elif answer.lower() == "yes":
        print("Let's play!")
        break
    else:
        print("Invalid input! Please enter either 'Yes' or 'No'.")
# Game modes
print("Choose a game mode")
game_mode = input("Game mode 1 -> (First to win), Game mode 2 -> (Two out of three)-")

# In game mode (1) we are creating a while loop which loops until the user or the computer wins the game
# We have couple of if elif statements where we check the user input and the random choice of the computer
# After we define who the winner is with a boolean flag that changes after the user wins, and we print out the winner

# Game mode -> 1
if game_mode == '1':
    print("Game mode 1 -> First to win")
    print("Lets play!")
    while True:
        computer_input = random.choice(choices)
        win = False
        while True:
            player_one_input = input("Choose your move: ")
            if is_valid_input(player_one_input, choices):
                break
            else:
                print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'.")

        if player_one_input == computer_input:
            print(f"Computer choose:{computer_input}")
            print("Draw")
            continue
        elif player_one_input == "rock" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        elif player_one_input == "paper" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        elif player_one_input == "scissors" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            win = True
            break
        else:
            print(f"Computer choose:{computer_input}")
            break

    if win:
        print("Congratulations! You win!")
    else:
        print(f"{computer} wins")

# In game mode (2) we are creating a while loop which loops until the user or the computer reaches two wins
# Every time the user or the computers wins we add +1 to a counter
# When the counter reaches 2 we break the while loop and print out the winner.

# Game mode - > 2
if game_mode == "2":
    print("Game mode 2 -> Two out of three")
    print("Lets play!")
    player_wins_counter = 0
    computer_wins_counter = 0
    while player_wins_counter < 2 and computer_wins_counter < 2:
        player_one_input = input("Choose your move:")
        computer_input = random.choice(choices)
        while True:
            player_one_input = input("Choose your move: ")
            if is_valid_input(player_one_input, choices):
                break
            else:
                print("Invalid input! Please enter either 'rock', 'paper', or 'scissors'.")
        if player_one_input == computer_input:
            print(f"Computer choose:{computer_input}")
            print("Draw")
        elif player_one_input == "rock" and computer_input == "scissors":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "paper" and computer_input == "rock":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        elif player_one_input == "scissors" and computer_input == "paper":
            print(f"Computer choose:{computer_input}")
            player_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")
        else:
            print(f"Computer choose:{computer_input}")
            computer_wins_counter += 1
            print(f"Player:{player_wins_counter} - Computer:{computer_wins_counter}")

    if player_wins_counter > computer_wins_counter:
        print("Congratulations! You win!")
    else:
        print("Computer wins!")

print(f"Thank you for playing {player_name}! See you soon!")
