from word_selection import choose_word
from game_logic import display_word, is_word_guessed, get_letter, check_guessed_letter, get_hint, display_output
from results_recording import update_results
from constants import MAX_WRONG_GUESSES, HINTS, HANGMAN_STAGES

def play_hangman(results):
    print("HANGMAN GAME")
    print("=" * 30)

    # Asks for players name and capitalizes. 
    player_name = input("Enter your name: ").strip().capitalize() 
    if player_name == "":
        player_name = "Player"

    print(f"\nWelcome, {player_name}!\n")

    # Gets secret word, category and difficulty level
    secret_word, category_name, difficulty_name = choose_word()

    correct_letters = []
    wrong_letters = []
    hints_used = 0

    print("\nWord has been chosen!")
    print(f"Category: {category_name}")
    print(f"Difficulty level: {difficulty_name}")
    print("Let's begin!")

    # play game - displays the secret word and asks user to guess the letter
    while len(wrong_letters) < MAX_WRONG_GUESSES and not is_word_guessed(secret_word, correct_letters):
        hidden_word = display_word(secret_word, correct_letters)

        display_output(hidden_word, wrong_letters, hints_used)

        guess = get_letter(correct_letters, wrong_letters)
        if guess == "hint":
            if hints_used < HINTS:
                hint_letter = get_hint(secret_word, correct_letters)
                hints_used += 1
                print(f"Hint used! The letter '{hint_letter}' is in the word.")
            else:
                print("No hints left.")
        else:
            check_guessed_letter(secret_word, guess, correct_letters, wrong_letters)

    # End results
    won = is_word_guessed(secret_word, correct_letters)

    if won:
        print(f"\nCongratulations, {player_name}!")
        print(f"You guessed the word: {secret_word.upper()}")
        print("=" * 30)
        
    else:
        print("\nGame over!")
        print(HANGMAN_STAGES[MAX_WRONG_GUESSES])
        print(f"The word was: {secret_word.upper()}")
        print("=" * 30)

    update_results(results, player_name, won, difficulty_name, hints_used)
   

# Asks user about play again option
def play_again():
    while True:
        answer = input("\nDo you want to play again? ").lower()

        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            
            return False
        else:
            print("Please enter yes or no.")