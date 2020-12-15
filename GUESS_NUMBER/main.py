import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
                print("Sorry, your guess was too low!")
        elif guess > random_number:
                print("Sorry, your guess was too high!")
    print(f"Success! You guessed the correct number of {guess}!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? Enter character: ")
        if feedback == 'h':
            high = guess
        elif feedback == 'l':
            low = guess + 1
    print(f"Success! I correctly guessed your number of {guess}!")

#guess(10)
computer_guess(10)