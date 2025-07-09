import time

def stopwatch(time):
    """
    Create a stopwatch, that counts to the time set
    """
    
    print("Starting the watch...")
    
    for second in range(time + 1):
        print(f"Time: {second} seconds", end="\r")
        time.sleep(1)
        
    print("\nStopwatch finished!")
    
if __name__ == "__main__":
    time = 10
    stopwatch(time)
    
    