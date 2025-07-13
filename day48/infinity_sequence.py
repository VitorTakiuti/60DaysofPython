import time

#generator of numbers

def infinity_numbers():
    num = 0 
    while True:
        yield num #this makes the code run without storing the data (numbers) 
        num += 1
        
generator = infinity_numbers()

for _ in range(10001): # '_' this doesnt store the numbers
    #time.sleep(1) this makes the code run a bit slower
    print(next(generator))