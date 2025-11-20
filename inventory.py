STARTING_ITEMS_IN_INVENTORY = 20

num_items = STARTING_ITEMS_IN_INVENTORY # <- restating the number 20


while num_items > 0: # <- This will only keep runing while num_items is greater than 0
    print("We have " + str(num_items) + " items in inventory.") # <- this prints the amount that we have
    
    to_buy = int(input("How many would you like to buy? "))
    
    if to_buy <= num_items:
        num_items -= to_buy # <- this is the same as num_items = num_items - to_buy
        if num_items > 0:
            print("Now we have " + str(num_items) + " left.")
    else:
        print("There is not enough in inventory for that purchase")
print("All out!") # <- this will only run once the num_items is 0
