import time

def infinity_ki():
    ki = 9000
    while True:
        yield f"Goku's Ki right now is {ki}"
        ki += 1000
        time.sleep(0.5)
        
goku_training = infinity_ki()

for _ in range(10): 
    print(next(goku_training))