# Create a rock, paper, scissors game as follows:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock
# - If both players choose the same, it's a tie
# Make it so that the user plays against the computer and
# can play multiple round, being able to track the score of
# the player and computer
#
# Organize the game in a class and make sure there is a function to end the match
# after the class, use a main to run the game

import random

class RockPaperScissors:
    """
    A class representing a Rock, Paper, Scissors game.

    Attributes:
        player_score (int): The score of the player.
        computer_score (int): The score of the computer.
        choices (list): The available choices for the game.

    Methods:
        play(): Starts the game and allows the player to play against the computer.
    """

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ['rock', 'paper', 'scissors']

    def play(self):
        """
        Starts the Rock, Paper, Scissors game.

        The player can play against the computer and track the score.
        """
        while True:
            while True:
                player_choice = input('Choose rock, paper or scissors: ').lower()
                if player_choice in self.choices:
                    break
                print('Invalid choice')
            computer_choice = random.choice(self.choices)
            print(f'Computer chose {computer_choice}')
            if player_choice == computer_choice:
                print('It\'s a tie!')
            elif player_choice == 'rock':
                if computer_choice == 'scissors':
                    print('You win!')
                    self.player_score += 1
                else:
                    print('You lose!')
                    self.computer_score += 1
            elif player_choice == 'scissors':
                if computer_choice == 'paper':
                    print('You win!')
                    self.player_score += 1
                else:
                    print('You lose!')
                    self.computer_score += 1
            elif player_choice == 'paper':
                if computer_choice == 'rock':
                    print('You win!')
                    self.player_score += 1
                else:
                    print('You lose!')
                    self.computer_score += 1
            else:
                print('Invalid choice')
            print(f'Player: {self.player_score} - Computer: {self.computer_score}')
            if input('Do you want to play again? user \'q\' to quit or enter to continue\n') == 'q':
                print(f'Final score: Player: {self.player_score} - Computer: {self.computer_score}')
                if self.player_score > self.computer_score:
                    print('You won the game!')
                elif self.player_score < self.computer_score:
                    print('You lost the game!')
                else:
                    print('It\'s a tie!')
                break

if __name__ == '__main__':
    game = RockPaperScissors()
    game.play()
