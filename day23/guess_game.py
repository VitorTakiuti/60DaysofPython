import random

def guess_game():
    """
    A game where the user guess a random number
    
    """
    
    print("Welcome to my number guesser game")
    
    secret_number = random.randint(0,100)
    
    attempts = 0 
    
    while True:
        try:
            guess = int(input("Tyoe your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print(f"Your guess {guess} is lower than the secret number")
            elif guess > secret_number:
                print(f"Your guess{guess} is higher than the secret number")
            else:
                print(f"Congratulation ! You found the secret number that was {secret_number}, your attemps were {attempts}")
                break
        
        except ValueError:
                print("Please type a valid number!")
                
if __name__ == "__main__":
    guess_game()

        