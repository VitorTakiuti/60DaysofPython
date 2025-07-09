def table(): 

    """
    This function receive a number and return the multiplication table of this number
    
    """
    
    try:
        
        number = int(input("Choose a number to get the multiplication table: "))
        
        print(f"\nMultiplication Table of {number}: ")
        
        for i in range(1,11):
            result = number * i 
            print(f"{number} x {i} = {result}")
            
    except ValueError:
        print("ïnvalid entry, Please type a number")
        
if __name__ == "__main__"
    table()