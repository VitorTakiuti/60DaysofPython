entrance = input("Choose a number: ")

try:
    number = int(entrance)
    if number % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
        
except ValueError:
    print("Your entance is not a Whole Number")