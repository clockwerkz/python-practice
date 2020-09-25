import random

numberOfGuesses = 0
answer = -1
numberToGuess = random.randint(1,20)
print("I am thinking of a number between 1 and 20")
while (answer != numberToGuess):
    print("Take a guess.")
    answer = int(input())
    numberOfGuesses+=1
    if (answer > numberToGuess):
        print("Your guess is too high.")
    if (answer < numberToGuess):
        print("Your guess is too low.")
    guessFormat = numberOfGuesses > 1  and " guesses!" or "guess!" #Python ternary operation
print("Good job! You guessed my number in " + str(numberOfGuesses) + guessFormat)