import random

min = 1
max = 100
num = random.randint(min,max)
n = input("Guess? ")

while True:
    try:
        guess = int(n)
        if guess == num:
            print("Correct")
            break
        elif guess < num:
            print("Low")
            n = input("Guess? ")
        elif guess > num:
            print("Hight")
            n = input("Guess? ")
    except ValueError:
        print("Please Enter a Number")
        n = input("Guess? ")
        
