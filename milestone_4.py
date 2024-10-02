#import necessary packages
import random

word_list1 = ["Bananna", "Satsuma", "Pear", "Strawberry", "Apple"]

# create class
class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.list_of_guesses = []
        self.word_guessed = [self.word_guessed.append("_") for letter in self.word if letter not in self.list_of_guesses]
        _unique_letters = set(list(self.word))
        self.num_letters = len(_unique_letters)
        self.num_lives = num_lives
        


hangman = Hangman(word_list1)

print(hangman)


#for letter in self.word:
            #self.word_guessed.append("_")