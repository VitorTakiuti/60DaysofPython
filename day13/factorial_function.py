def factorial(n):
    """
    Calculate the fatorial of a number
    
    Return the Factorial of n
    """
    if n < 0:
        raise ValueError("The number must be positive")
    
    #if n = 0 or 1, the result is always 1. 
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))

try: 
    print(f"Factorial equals {factorial(1)}")
except ValueError as e:
    print(e)