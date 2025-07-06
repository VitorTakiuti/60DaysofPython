import random
import string 

def password_generator(size):
    lengh = size 
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''
    
    while len(password) < size: 
        password += random.choice(characters)
        
    print(f"Your Random password is {password}")
    
#password with 30 characters
print(password_generator(30))