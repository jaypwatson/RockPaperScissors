# RockPaperScissors

The code is a simple Python program that allows you to play a best 2 out of 3 rounds game of Rock Paper Scissors. Here's how it works:

1. The program starts by importing the `random` module, which is used to generate random choices for the computer player.
2. It then defines the valid choices for the game (rock, paper, and scissors) and prints out instructions for the user.
3. The program initializes the scores for both the user and the computer to 0.
4. The program then enters a loop that plays 3 rounds of Rock Paper Scissors. In each round:
    - The program prompts the user to enter their choice and converts it to lowercase using the `lower()` method.
    - It then checks if the user's choice is one of the valid options. If not, it prints an error message and skips to the next iteration of the loop.
    - If the user's choice is valid, the program uses the `random.choice()` method to randomly select a choice for the computer from the list of valid choices.
    - The program then determines the winner of the round based on the rules of Rock Paper Scissors. If the user's choice beats the computer's choice, the user wins the round and their score is incremented by 1. If the computer's choice beats the user's choice, the computer wins the round and their score is incremented by 1. If both choices are the same, it's a tie and no one's score is incremented.
    - The program prints out the result of the round.
5. After all 3 rounds have been played, the program compares the final scores of both players to determine who won the game. It then prints out the final result.

That's how this Rock Paper Scissors game works! 😊
