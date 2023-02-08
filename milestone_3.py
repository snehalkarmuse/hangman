def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            print("Good Guess.")
            break
        else:
            print("Oops! That is not a valid input.")
    check_guess(guess)

def check_guess(guess): 
    guess = guess.lower()
    if guess in word:
        print(f"Good guess {guess} is in the word. ")
    else:
        print(f"Sorry {guess} is not in the word. Try again.")

ask_for_input()