import time

def sec_stopwatch():
    """
    Create a 10 seconds stopwatch
    """
    print("Stopwatch of 10 Seconds")
    
    timeinseconds = 10
    
    while time > 0: 
        print(f"Time left: {time} seconds", end="\r", flush=True)
        time.sleep(1)
        timeinseconds -= 1
        
    print("\nStopwatch has finished!")
    
if __name__ == "__main__":
    sec_stopwatch()
    