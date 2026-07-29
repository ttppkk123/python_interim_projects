import random
from constants import MAX_WRONG_GUESSES, HINTS, HANGMAN_STAGES

# Displays the secret word 
def display_word(secret_word, correct_letters):
    hidden_word = ""

    for letter in secret_word:
        if letter in correct_letters:
            hidden_word += letter.upper() + " "
        else:
            hidden_word += "_" + " "

    return hidden_word.strip()

# Check if all letters in the hidden word are guessed
def is_word_guessed(secret_word, correct_letters):
    for letter in secret_word:
        if letter not in correct_letters:
            return False

    return True

# Gets letter from the user and checks if it is already guessed
def get_letter(correct_letters, wrong_letters):
    while True:
        guess = input("\nGuess a letter: ").lower()

        if guess == "hint":
            return "hint"
        elif len(guess) != 1:
            print("Please enter only one letter.")
        elif not guess.isalpha():
            print("Please enter only letters.")
        elif guess in correct_letters or guess in wrong_letters:
            print("You already guessed that letter.")
        else:
            return guess


# Checks guessed letter
def check_guessed_letter(secret_word, guess, correct_letters, wrong_letters):
    if guess in secret_word:
        correct_letters.append(guess)
        print("Correct!")
    else: 
        wrong_letters.append(guess)
        if len(wrong_letters)==MAX_WRONG_GUESSES:
            print("Wrong Letter!")
        else: 
            print("Wrong Letter, try again!")
            print("If you need help, type HINT")


# Gives user one letter from the secret word that has not been guessed yet
def get_hint(secret_word, correct_letters):
    available_letters = []

    for letter in secret_word:
        if letter not in correct_letters and letter not in available_letters:
            available_letters.append(letter)

    hint_letter = random.choice(available_letters)
    correct_letters.append(hint_letter)

    return hint_letter

# Prints results: word with guessed letters, wrong letters, hints left and hangman stage
def display_output(hidden_word, wrong_letters, hints_used):

    print("\n" + "-" * 30)
    print("Word:", hidden_word)
    if len(wrong_letters) == 0:
        print("Wrong guesses: None")
    else:
        print("Wrong guesses:", ", ".join(wrong_letters).upper())
    print("Guesses left:", MAX_WRONG_GUESSES - len(wrong_letters))
    print("Hint left:", HINTS - hints_used)
    print(HANGMAN_STAGES[len(wrong_letters)])
    print("-" * 30)