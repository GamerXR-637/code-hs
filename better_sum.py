n_one = int(input("Please enter a number? ")) # < ask the starting value
n_two = int(input("Please enter another number? ")) # < asks the ending value

sum = 0 # < Rule: n + 0 = n || so that why we start with 0
for i in range(n_one,n_two+1): # < we run it for i times from n_one to n_two+1 << [We want to include n_two in the sum]
    sum = sum + i # < adds i to the sum

print(sum)
