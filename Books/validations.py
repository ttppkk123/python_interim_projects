from constants import MIN_PUBLICATION_YEAR, MAX_PUBLICATION_YEAR

# Convert input to float
def input_float(value):
    while True:
        try:
            return float(input(value)) 
        except ValueError:
            print("Error: Please enter a valid number.")

# Convert input to int
def input_int(value):
    while True:
        try:
            return int(input(value))
        except ValueError:
            print("Error: Please enter a valid number.")


# Get non-empty text input
def input_text(value):
    while True:
        text = input(value).strip()

        if text:
            return text
        else:
            print("Error: This field cannot be empty.")


# Validate year input
def input_year(value):
    while True:
        try:
            year = int(input(value))
            if year < MIN_PUBLICATION_YEAR or year > MAX_PUBLICATION_YEAR:
                print(f"Error: Year must be between {MIN_PUBLICATION_YEAR} and {MAX_PUBLICATION_YEAR}.")
            else: 
                return year

        except ValueError:
            print("Please enter a valid year.")