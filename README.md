# Hangman

## Contents:

- Synopsis
- File structure
- Installation
- How to use Hangman game
- License info

## Synopsis

The aim of this project is to make a Hangman game in python. It will take letters as user inputs as guesses which will then be checked to see if the word contains the guessed letter. This is a chance to apply the python I have been learning through the AI core bootcamp.

## File Structure

The project currently has three python files, which serve to document the stages of developing the hangman game. Please note, the first milestone was simply creating the GitHub repository, hence the files start at "milestone_2.py". 

**"milestone_2.py":** This file creates a list of possible words to generate and selects a random word out of the list. Additionally, there is code that checks if the user input is a single character. 

**"milestone_3.py":** This file goes through the process of taking a valid user input and checking if the inputted letter is in the word. At the end of this milestone, two functions are created, "check_guess" and "ask_for_input". "ask_for_input" makes sure the user input is valid and then calls "check_guess" to check if the guesses letter is in the word.

**"milestone_4.py":** This file creates a class for the hangman game, named "Hangman", which has paramaters of a list of words and number of lives (default set to 5 lives). Within this class, there are two methods defined, check_guess and ask_for_input. They have similar functionality to the functions of the same name defined in "milestone_3.py" with some additional functionality. The check_guess method now appends correct guesses to the list of characters in the word (self.word_guessed), which will allow you to see where in the word your correct guessed letters are placed. Additionallly, when the user inputs an incorrect guess, the number of lives now decreases by 1. The only notable change to the ask_for_input method is that it now adds guesses to a list of all guesses so that you get a message stating you have already guessed the letter if that is the case.

**"milestone_5.py":** This file uses the hangman class created in "milestone_4.py" and creates a function that calls and instance of the class. The function runs a while loop with conditions that break the loop if the number of lives is equal to 0 and if the number of unique letters left to guess is 0. It is not in perfect working order, as pressing the enter key when asked for an input does count as a correct guess. However, for learning purposes, I have got the most out of this project and will try fixing the issue in my spare time.

## Installation

To install the hangman game, just download "milestone_5.py" and run the file in the shell (I use Bash as I'm on linux) using the command "python milestone_5.py", making sure the file is in your current working directory. Note that I have conda environment installed, otherwise "python3 milestone_5.py" would be used instead to run the file.

## How to use the hangman game

Once you have run the "milestone_5.py" file, you will be asked to input a letter to guess. You will recieve a message in the telling you if the guess was correct or not, or if the guess was not valid or you have already guessed this letter. The game will end when your lives are equal to 0 (in which case you lose) or if the number of unique letters left is equal to zero (in which case you win)