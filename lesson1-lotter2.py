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

        # DRY applied
        guess = int(user_input)
        if guess not in WINNER:
            num_of_guesses += 1
        else:
            if guess in correct_answers:
                print(f"You already guessed {guess}. Try again.")
            else:
                correct_answers.add(guess)
                print(f"Awesome, {guess} is indeed a winning number!")

        # Feedback shown after every guess, but not on the final win
        if len(correct_answers) < len(WINNER):
            print(f"You currently have {len(correct_answers)} correct answers.")

    print("Congratulations!")  # This only runs when the while loop breaks
    return num_of_guesses


def print_leaderboard(leaderboard):
    # sorting - score is first item in sub-list
    leaderboard.sort()

    # Headers for the table
    headers = ["Name", "Score"]

    # Table
    print("|-------------------|")
    print(f"| {headers[0]:<10}| {headers[1]:<5}|")
    print("|-------------------|")
    for score, name in leaderboard:  # Don't forget we did score first, THEN name
        print(f"| {name:<10}| {score:<5}|")
    print("|-------------------|")


while True:
    player_name = input("Enter your name to play: ")

    result = play_lottery(player_name)

    if result is None:
        print(f"{player_name} quit the game.")
    else:
        # We store result (score) first so .sort() works automatically
        leaderboard.append([result, player_name])
        print(f"{player_name} guessed the number in {result} guesses.")

    again = input("Does anyone else want to play? (y/n): ")
    if again == "n":
        break

print_leaderboard(leaderboard)
