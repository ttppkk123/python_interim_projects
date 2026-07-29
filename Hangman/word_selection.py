import random
from constants import WORD_FILE, CATEGORY_NAMES, DIFFICULTY_NAMES

# Asks user to choose category
def choose_category():
    print("Choose a category:")
    print("-" * 30)
    for number in CATEGORY_NAMES:
            print(f"{number}. {CATEGORY_NAMES[number]}")
    print("-" * 30)

    while True:
        choice = input("Enter category number: ")

        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


# Asks user to choose difficulty level
def choose_difficulty():
    print("Choose difficulty level:")
    print("-" * 30)
    for number in DIFFICULTY_NAMES:
        print(f"{number}. {DIFFICULTY_NAMES[number]}")
    print("-" * 30)

    while True:
        choice = input("Enter difficulty level: ")

        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


# Reads word.txt file and returns eligible words based on the difficulty level 
# and category received from the user
def get_words(category, difficulty):
    eligible_words = []
    
    with open(WORD_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            file_category = int(parts[0])
            file_difficulty = int(parts[1])
            file_word = parts[2]

            if file_category == category and file_difficulty == difficulty:
                eligible_words.append(file_word)

    return eligible_words

# Randomly chooses word based on the input on the dificulty level 
# and category received from the user
def choose_word():
    category = choose_category()
    difficulty = choose_difficulty()
    words = get_words(category, difficulty)
    random_word = random.choice(words)
    category_name = CATEGORY_NAMES[category]
    difficulty_name = DIFFICULTY_NAMES[difficulty]
    return random_word, category_name, difficulty_name