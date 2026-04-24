# Tuple of 3 winning numbers
WINNER = (1, 4, 9)

# Define scoreboard
leaderboard = []  # Was Dict, but sorting shucks :D


def play_lottery(player_name):
    num_of_guesses = 0  # putting this in the function so it resets when func is called
    correct_answers = set()
    while len(correct_answers) < len(WINNER):
        user_input = input("Guess the number: ")

        if user_input.lower() in ["q", "quit"]:
            return None

        if not user_input.isnumeric():  # if it's not a number catch it
            print("Invalid input. Please enter a number.")
            continue
        elif int(user_input) not in WINNER:
            num_of_guesses += 1
        else:
            if int(user_input) in correct_answers:
                print(f"You already guessed {int(user_input)}. Try again.")
            else:
                correct_answers.add(int(user_input))
                print(f"Awesome, {user_input} is indeed a winning number!")
        print(f"You currently have {len(correct_answers)} correct answers.")
    print("Congratulations!")
    return num_of_guesses


def print_leaderboard(leaderboard):
    # sorting
    leaderboard.sort()

    # Headers for the table
    headers = ["Name", "Score"]

    # Table
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
        leaderboard.append((result, player_name))  # Drop the 'list' into the list :D, do it score first to use for sorting later
        print(f"{player_name} guessed the number in {result} guesses.")

    again = input("Does anyone else want to play? (y/n): ")
    if again == "n":
        break

print_leaderboard(leaderboard)
