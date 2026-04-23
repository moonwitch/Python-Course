# Predefine number
# Declare constant value for winning
WINNER = 8

# Define scoreboard
leaderboard = {}


def play_lottery(player_name):
    # Handles 1 player
    # runs the loop and checks for q as exit
    # output is number of guesses
    num_of_guesses = 0  # putting this in the function so it resets when func is called
    while True:
        user_input = input("Guess the number: ")

        if user_input.lower() in ["q", "quit"]:
            return None

        if not user_input.isnumeric():
            print("Invalid input. Please enter a number.")
            continue
        elif int(user_input) != WINNER:
            num_of_guesses += 1
        else:
            return num_of_guesses


def print_leaderboard(leaderboard):
    headers = ["Name", "Score"]
    print("|-------------------|")
    print(f"| {headers[0]:<10}| {headers[1]:<5}|")
    print("|-------------------|")
    for name, score in leaderboard.items():
        print(f"| {name:<10}| {score:<5}|")
    print("|-------------------|")


while True:
    player_name = input("Enter your name to play: ")

    result = play_lottery(player_name)

    if result is None:
        print(f"{player_name} quit the game.")
    else:
        leaderboard[player_name] = result
        print(f"{player_name} guessed the number in {result} wrong guesses.")

    again = input("Does anyone else want to play? (y/n): ")
    if again == "n":
        break

print_leaderboard(leaderboard)
