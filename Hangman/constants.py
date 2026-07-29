# Number of tries player is given per game
MAX_WRONG_GUESSES = 6

# Number of hints player is given per game
HINTS = 2

# file where random word is selected from
WORD_FILE = "words.txt"

# File where results of the game is stored
RESULTS_FILE = "results.csv"

# Dict for categories
CATEGORY_NAMES = {
    1: "Animals",
    2: "Countries",
    3: "Foods & Drinks",
    4: "Adjectives"
}

# Dict for difficulty levels
DIFFICULTY_NAMES = {
    1: "Easy",
    2: "Medium",
    3: "Hard"
}

# Array for the hangman stages
HANGMAN_STAGES = [
"""
  +---+
  |   |
      |
      |
      |
      |
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
""",
"""
  +---+
  |   |
  O   |
 /    |
      |
      |
""",
"""
  +---+
  |   |
  O   |
 / \\  |
      |
      |
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
"""
    ]