# Predefine number
# User has to guess the number
# Declare constant value for winning
WINNER = 8

# Declare input to var
name = input("Enter your name: ")
user_input = input("Guess the number: ")
num_of_guesses = 0

while True:
    print("You guessed it! The number was", WINNER)
    print("That took", num_of_guesses, "guesses")

    if user_input == "q" or user_input == "Q":
        break
    elif int(user_input) != WINNER:
        user_input = input("Guess the number: ")
        num_of_guesses += 1