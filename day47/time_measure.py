#decorators

import time

#creating the decorator
def time_measure_execute(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"The Total time of the function was: {total_time}")
        return result
    return wrapper  

@time_measure_execute  #it must be right next to each other, no space lines between them
def task_1():
    print("Function is runnig...")
    time.sleep(2)
    print("Function has ended")
    
@time_measure_execute
def task_2():
    print("Function is runnig...")
    time.sleep(3)
    print("Function has ended")
    
task_1()

task_2()