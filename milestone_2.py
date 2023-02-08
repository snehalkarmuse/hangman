import random

word_list = ["Mango","Banana","Apple","Orange","Grapes"]
print(word_list)
word = random.choice(word_list)
print(word)
guess = input("Enter a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess.")
else:
    print("Oops! That is not a valid input.")