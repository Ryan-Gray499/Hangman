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

The project currently has two python files, which serve to document the stages of developing the hangman game. Please note, the first milestone was simply creating the GitHub repository, hence the files start at "milestone_2.py". This file creates a list of possible words to generate and selects a random word out of the list. Additionally, there is code that checks if the user input is a single character. "milestone_3.py" goes through the process of taking a valid user input and checking if the inputted letter is in the word. At the end of this milestone, two functions are created, "check_guess" and "ask_for_input". "ask_for_input" makes sure the user input is valid and then calls "check_guess" to check if the guesses letter is in the word.
