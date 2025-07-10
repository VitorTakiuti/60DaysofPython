import math

def square_root(number):
    """
    Calculate the square root of any number
    
    number(float)
    
    return float
    """
    
    if number < 0:
        raise ValueError("It isn't possible to calculate, please use a Positive number!" )
    
    
    return round(math.sqrt(number), 2)

if __name__ == "__main__":
    print(square_root(144))