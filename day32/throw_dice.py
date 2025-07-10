import random
#from random import randint
def throw_dice():
    """
    Simulate a dice throw with six sides
    
    return: int 
    """
    
    return random.randint(1, 6)

if __name__ == "__main__":
    print(f"The result of the dice is: {throw_dice()}")