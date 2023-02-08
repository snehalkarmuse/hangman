import random

word_list = ["Mango","Banana","Apple","Orange","Grapes"]
print(word_list)
word = random.choice(word_list)
print(word)
while True:
    guess = input("Enter a letter: ")
    if len(guess) == 1 and guess.isalpha():
        print("Good Guess.")
        break
    else:
        print("Oops! That is not a valid input.")

if guess in word:
    print(f"Good guess {guess} is in the word. ")
else:
    print(f"Sorry {guess} is not in the word. Try again.")
    