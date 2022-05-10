

word_list = ["Bottle","Love", "marrege"]

import random

chosen_word = random.choice(word_list)
print(f"Passt, the solution is {chosen_word}")

dispaly = []
word_length = len(chosen_word)
for _ in range(word_length):
    dispaly += "_"
print(dispaly)


guess = input("Guess a letter ").lower()
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        dispaly[position] = letter
    
print(dispaly)