# take a guess from user and check it is valid input
while True:
    guess = input("Please guess a letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")