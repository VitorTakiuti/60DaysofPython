#this counter will count any number set by the user

def counter():
    try:
        limit = int(input("Type the maximum value for the counter: "))
                    
        for i in range(limit):
            print(i)
            if i == limit:
                print("The counter reach its limit")
                break 
    
    except ValueError:
        print("Invalid entry, please type a whole number")

counter()
    