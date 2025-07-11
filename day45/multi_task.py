#threads are smaller tasks that the computer run at the same time

import threading
import time

def task(name, execution_time):
    print(f"Task {name} started...")
    time.sleep(execution_time)
    print(f"Task {name} ended...")
    
thread1 = threading.Thread(target=task, args=("Download task1", 3))
thread2 = threading.Thread(target=task, args=("Download task2", 4))

#Starting the tasks
thread1.start()
thread2.start()

#waiting for them 
thread1.join()
thread2.join()

print("All Tasks are done!")

# if I run like this, it will take 9 seconds, because the tasks are not running at the same time
# the first task needs to be completed so the second task start
# This is not "Multi Taking"
# print(task("Download 1", 3))
# print(task("Download 2", 6))