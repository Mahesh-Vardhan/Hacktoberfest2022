import random
n = random.randint(1, 100)
guess = 0

while guess != n:
    guess = int(input("Enter any number: "))
    
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high!")
        
print("You guessed it right!!")
