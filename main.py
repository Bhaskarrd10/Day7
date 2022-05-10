

word_list = ["Bottle","Love", "marrege"]

import random

chosen_word = random.choice(word_list)
print(f"Passt, the solution is {chosen_word}")

dispaly = []
word_length = len(chosen_word)
for _ in range(word_length):
    dispaly += "_"
print(dispaly)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position:{position}\n Current letter: {letter}\n                 Gussed letter: {guess}")
        if letter == guess:
            dispaly[position] = letter
        
    print(dispaly)

    if "_" not in dispaly:
        end_of_game = True
        print("You win")
    