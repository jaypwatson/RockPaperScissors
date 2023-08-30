import random

# Define the choices
choices = ['rock', 'paper', 'scissors']

# Print the instructions
print('Welcome to Rock Paper Scissors!')
print('To play, enter your choice: rock, paper, or scissors.')
print('The game is best 2 out of 3 rounds.')

# Initialize the scores
user_score = 0
computer_score = 0

# Play 3 rounds
for round in range(3):
    # Get the user's choice
    user_choice = input(f'Round {round + 1} - Your choice: ').lower()

    # Validate the user's choice
    if user_choice not in choices:
        print('Invalid choice. Please try again.')
    else:
        # Get the computer's choice
        computer_choice = random.choice(choices)
        
        # Determine the winner
        if user_choice == computer_choice:
            print(f'It\'s a tie! You both chose {user_choice}.')
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(f'You win this round! You chose {user_choice} and the computer chose {computer_choice}.')
            user_score += 1
        else:
            print(f'You lose this round! You chose {user_choice} and the computer chose {computer_choice}.')
            computer_score += 1

# Print the final result
if user_score > computer_score:
    print(f'You win the game with a score of {user_score}-{computer_score}!')
elif user_score < computer_score:
    print(f'You lose the game with a score of {user_score}-{computer_score}.')
else:
    print(f'The game is a tie with a score of {user_score}-{computer_score}.')
