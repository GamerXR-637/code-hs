import random # <- importing the library of random from Python

for i in range (1, 101): # <- we want to count from 1 to 100 
    die_roll = random.randint(1,6) # <- get a random value from 1 to 6, including 1, and 6
    print(die_roll) # <- print it into the console 
