fibonacci = [0, 1] #sequence always start with 0 and 1 

for i in range(8): #First 8 numbers in the fibonacci sequence
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_number)
    
print(fibonacci)