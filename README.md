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
