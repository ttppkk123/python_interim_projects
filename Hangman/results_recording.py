import csv
from constants import RESULTS_FILE

# Updates results of each game played
def update_results(results, player_name, won, difficulty_name, hints_used):
    if player_name not in results:
        results[player_name] = {
            "Played": 0,
            "Won": 0,
            "Lost": 0,
            "Easy": 0,
            "Medium": 0,
            "Hard": 0,
            "Hints Used": 0
        }

    results[player_name]["Played"] += 1
    results[player_name]["Hints Used"] += hints_used

    if won:
        results[player_name]["Won"] += 1

        if difficulty_name == "Easy":
            results[player_name]["Easy"] += 1
        elif difficulty_name == "Medium":
            results[player_name]["Medium"] += 1
        elif difficulty_name == "Hard":
            results[player_name]["Hard"] += 1
    else:
        results[player_name]["Lost"] += 1


# Records results in the CSV file
def record_results(results):

    max_wins = 0

    for player_name in results:
        if results[player_name]["Won"] > max_wins:
            max_wins = results[player_name]["Won"]

    with open(RESULTS_FILE, "w", newline="") as file:
        fieldnames = ["Player Name", "Played", "Won", "Lost", "Easy", "Medium", "Hard", "Hints Used", "Winner"]
        writer = csv.DictWriter (file, fieldnames)
        writer.writeheader()

        for player_name in results:
            
            player_results = results[player_name]

            if max_wins > 0 and player_results["Won"] == max_wins:
                winner = "Yes"
            else:
                winner = "No"

            writer.writerow({
                "Player Name": player_name,
                "Played": player_results["Played"],
                "Won": player_results["Won"],
                "Lost": player_results["Lost"],
                "Easy": player_results["Easy"],
                "Medium": player_results["Medium"],
                "Hard": player_results["Hard"],
                "Hints Used": player_results["Hints Used"],
                "Winner": winner
            })



# Prints results in the console
def print_results():
    with open(RESULTS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n" + "-" * 30)
        print("SAVED RESULTS")
        print("-" * 30)

        print(
            f"{'Player':<15}"
            f"{'Played':<8}"
            f"{'Won':<6}"
            f"{'Lost':<6}"
            f"{'Easy':<6}"
            f"{'Medium':<8}"
            f"{'Hard':<6}"
            f"{'Hints':<10}"
            f"{'Winner':<8}"
        )

        for row in reader:
            print(
                f"{row['Player Name']:<15}"
                f"{row['Played']:<8}"
                f"{row['Won']:<6}"
                f"{row['Lost']:<6}"
                f"{row['Easy']:<6}"
                f"{row['Medium']:<8}"
                f"{row['Hard']:<6}"
                f"{row['Hints Used']:<10}"
                f"{row['Winner']:<8}"
            )

        print("-" * 30)
