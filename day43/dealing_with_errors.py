def divide(nominator, denominator):
    try:
        result = numerator / denominator
        print(f"Thes result of the Division is {result}!")
        
    except ZeroDivisionError:
        print("0 Cannot be the divider or the denominator")
    
    except TypeError:
        print("Code cannot acept strings, just numbers!")
    
    print("Function worked!")
    
if __name__ == "__main__":
    divide(5,2)