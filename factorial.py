n = int(input("Value of n? ")) # <- asks the user for a input 
m = 1 # <- we start with 1 because 1 * n is n and so on 
for j in range(1,n+1): # <- we want to loop this from 1 and multiply j by m (if it was 0, then it results 0 due to 0 * n = 0) and we want to include n, so n + 1 includes n
    m = m * j # < repeated mutipucation 
print(m)
