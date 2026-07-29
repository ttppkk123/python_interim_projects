from game_loop import play_hangman, play_again
from results_recording import record_results, print_results

results = {}

while True:
    play_hangman(results)

    if not play_again():
        record_results(results)
        print_results()
        print("\nThanks for playing Hangman!")
        print("=" * 30)
        break