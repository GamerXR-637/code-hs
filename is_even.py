SENTINEL = 0
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
while True:
    number = int(input("Enter a number: "))
    if number == SENTINEL:
        print("Done!")
        break
    else:
        if is_even(number) == True:
            print("Even")
        else:
            print("Odd")
