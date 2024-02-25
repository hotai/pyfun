import json
import random

word_list = []

def load_json():
    global word_list
    with open('words.json') as f:
        data = json.load(f)
        word_list = data['data']

def get_word():
    if not word_list: load_json()
    return random.choice(word_list)

def draw_hangman(step, hanged=False):
    if step == 1:
        print("____________\n" +
              "|          " + ("|" if hanged else ""))
    elif step == 2:
        draw_hangman(1, hanged)
        print("           O")
    elif step == 3:
        draw_hangman(2, hanged)
        print("           |")
    elif step == 4:
        draw_hangman(2, hanged)
        print("          /|")
    elif step == 5:
        draw_hangman(2, hanged)
        print("          /|\\")
    elif step == 6:
        draw_hangman(5, hanged)
        print("          / ")
    elif step == 7:
        draw_hangman(5, hanged)
        print("          / \\""")
    elif step == 8:
        draw_hangman(7, True)

def play():
    word = get_word()
    while len(word) > 6 or ' ' in word or '-' in word:
        word = get_word()
    word = word.upper()
    guessed_word = list("_" * len(word))
    print("Word: " + ("_ " * len(word)))
    bad_guesses = 0
    while "".join(guessed_word) != word and bad_guesses < 8:
        guess = input("Enter your guess: ").upper()
        if guess in word:
            for n in range(len(guessed_word)):
                if word[n] == guess: guessed_word[n] = guess
            print("Correct! " + str(guessed_word))
        else:
            print("Oopsie daisy...")
            bad_guesses += 1
            draw_hangman(bad_guesses, True if bad_guesses >= 8 else False)
        
    # check win/lose
    if bad_guesses == 8:
        print(f"Sorry, bruh, you're a loser! The word was '{word}'.")
    elif "".join(guessed_word) == word:
        print(f"You rock, bruh! The word is '{word}'.")
    else:
        print("WTH??")

# Les play!
play()
