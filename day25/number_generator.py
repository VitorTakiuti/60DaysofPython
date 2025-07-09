import random

def random_number_generator():
    """
    This function generates a sequence of 10 random numbers in a list
    """
    print("Welcome to the Random Number Generator")
    
    random_numbers = []
    
    for i in range(10):
        number = random.randint(1, 100)
        random_numbers.append(number)
        
    print("\nThe Random Numbers Generated are: ")
    for i, number in enumerate(random_numbers, start=1):
        print(f"Number {i}: {number}")
        
if __name__ == "__main__":
    random_number_generator()