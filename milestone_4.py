#import necessary packages
import random

word_list1 = ["Bananna", "Satsuma", "Pear", "Strawberry", "Apple"]

# create class
class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_guessed = ["_" for letter in self.word if letter not in self.list_of_guesses]
        _unique_letters = set(list(self.word))
        self.num_letters = len(_unique_letters)
        self.num_lives = num_lives
    
    def check_guess(self, guessed_letter):
        guessed_letter = guessed_letter.lower()
        if guessed_letter in self.word:
            print(f"Good guess, {guessed_letter} is in word")
            for letter in self.word:
                if letter == guessed_letter:
                    self.word_guessed[self.word.index(letter)] = guessed_letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guessed_letter} is not in word")
            print(f"you havve {self.num_lives}")
    
    def ask_for_input(self):
        while True:
            guessed_letter = input("Please guess a letter: ")
            if len(guessed_letter) == 1 and guessed_letter.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guessed_letter in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guessed_letter)
                self.list_of_guesses.append(guessed_letter)
        


hangman = Hangman(word_list1)

hangman.ask_for_input()


#for letter in self.word:
            #self.word_guessed.append("_")