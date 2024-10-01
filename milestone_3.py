# import necessary packages
import random

# Create list of words
word_list = ["Bananna", "Satsuma", "Pear", "Strawberry", "Apple"]

# get random word from the list
random_word = random.choice(word_list)
random_word = random_word.lower()
print(random_word)


# take a guess from user and check it is valid input
#while True:
    #guess = input("Please guess a letter: ")
    #if len(guess) == 1 and guess.isalpha() == True:
        #break
    #else:
        #print("Invalid letter. Please, enter a single alphabetical character.")


# check if guess is in word
#if guess in random_word:
    #print(f"Good guess, {guess} is in word")
#else:
    #print(f"sorry, {guess} is not in the word")


# Create function to check if guess is in the word

def check_guess(user_guess):
    user_guess.lower()
    if user_guess in random_word:
        print(f"Good guess, {user_guess} is in word")
    else:
        print(f"sorry, {user_guess} is not in the word")


# create function that asks user for an input

def ask_for_input():
    while True:
        guessed_letter = input("Please guess a letter: ")
        if len(guessed_letter) == 1 and guessed_letter.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guessed_letter)

ask_for_input()