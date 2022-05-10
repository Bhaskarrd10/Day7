import random

word_list = ["Bottle","Love", "marrege"]

chosen_word = random.choice(word_list)
print(f"Passt, the solution is {chosen_word}")

dispaly = []
for _ in range(len(chosen_word)):
    dispaly += "_"
print(dispaly)
guess = input("Guess a letter ").lower




for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")