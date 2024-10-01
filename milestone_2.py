import random

# create list
word_list = ["Bananna", "Satsuma", "Pear", "Strawberry", "Apple"]
print(word_list)

# get random element of list
word = random.choice(word_list)
print(word)

# get user input letter
guess = input("Guess a letter")

if len(guess) <= 1:
    print("Good guess!")
else:
    print("Oops, not a valid guess")