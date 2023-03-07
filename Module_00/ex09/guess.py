import random

secret_number = random.randint(1, 99)
num_guesses = 0

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")

while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        break
    elif not guess.isdigit():
        print("That's not a number.")
        continue

    num_guesses += 1
    guess = int(guess)

    if guess == secret_number:
        if guess == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if num_guesses == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in", num_guesses, "attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
