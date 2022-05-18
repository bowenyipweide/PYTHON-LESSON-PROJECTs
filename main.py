import random
from hangman_art import logo, stages
from hangman_wordlist import word_list

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
game_is_finished = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(display)
while not game_is_finished:
    print(f"Chosen word: {chosen_word}")
    guess = input("Guess a letter: ")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word:
        print(f"You have guessed {guess}, that's not in the word. You lost a life")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose")
    if not "_" in display:
        game_is_finished = True
        print("You manage to guess the word! You WIN!")

    print(stages[lives])
