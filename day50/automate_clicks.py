import pyautogui # pip install pyautogui in the right python version that you are using
import time

print("Position the mouse at the screen and wait 5 seconds...")

#print(pyautogui.position()) 
# or 
#position = pyautogui.position()
#print(position) # show mouse position currently

# x, y = pyautogui.position()
# pyautogui.click(x, y)
# print(f"Clicked at the position: x = {x} and y = {y}.")

#LOOP
while True:
    
    #Test 1
    time.sleep(5)
    x, y = 754, 680
    pyautogui.click(x, y)
    print(f"Clicked at the first position: x = {x} and y = {y}.")

    time.sleep(5)
    x, y = 507, 554
    pyautogui.click(x, y)
    print(f"Clicked at the second position: x = {x} and y = {y}.")






