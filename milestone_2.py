word = "hello"

set1 = set(list(word))

print(set1)
print(len(set1))

import random

# create list
word_list = ["Bananna", "Satsuma", "Pear", "Strawberry", "Apple"]
print(word_list)

# get random element of list
random_word = random.choice(word_list)
print(random_word)

# get user input letter
guess = input("Guess a letter")

# check input is a single character
if len(guess) <= 1:
    print("Good guess!")
else:
    print("Oops, not a valid guess")