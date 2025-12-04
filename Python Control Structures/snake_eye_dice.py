import random # <- we want to call the library

counter = 0

while True: # <- this will loop forever
    die_1 = random.randint(1,6) # <- this varable will change every time and be a number from 1 to 6
    die_2 = random.randint(1,6) # <- this varable will change every time and be a number from 1 to 6 
    counter += 1 # <- increase the amount of time it took to get 1,1
    # counter -= -1 # <- you can use this for funny 
    print("Rolled: " + str(die_1) + " " + str(die_2))
    if die_1 == die_2 and die_1 == 1: # <- this will check if it equal and if die_1 is equal to 1
        print("It took you " + str(counter) + " rolls to get snake eyes.")
        break
