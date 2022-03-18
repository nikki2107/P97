import random 

rightnumber = random.randint(1,9)

print("Number Guessing game")

chances=0

while chances <5:
    guess = int(input("Enter your guess "))
    chances=chances+1

    
    if guess<rightnumber:
        print("Too low! Guess a number higher than ",guess)

    if guess>rightnumber:
        print("Too high! Guess a number lower than ",guess)

    if guess == rightnumber:
        print("Congratulations...you won!! ")
        break

    if not chances <5:
        print ("You lose!! The correct answer is ",rightnumber)
