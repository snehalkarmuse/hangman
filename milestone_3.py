while True:
    guess = input("Enter a letter: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good Guess.")
        break
    else:
        print("Oops! That is not a valid input.")
