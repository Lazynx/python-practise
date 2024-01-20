from random import randint

the_number = randint(1, 20)
print("Hello! What is your name? ")
name = input()
print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
guesses = 1

while True:
    guess = int(input("Take a guess.\n"))

    if not (1 <= guess <= 20):
        print("\nYour guess not in 1 - 20.")
    if guess < the_number:
        print("\nYour guess is too low.")
    elif guess > the_number:
        print("\nYour guess is too high.")
    elif guess == the_number:
        print(f"\nGood job, {name}! You guessed my number in {guesses} guesses!")
        break
    guesses += 1
