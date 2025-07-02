# Curiosity: In Brazil the age limit is 18
def can_drive(age):
    age = int(age)
    if age >= 16:
        return True
    else:
        return False

#you cannot put strings as values in this scenario   
try:
    input_user = int(input("Type your age: "))
    print(can_drive(input_user))
except ValueError:
    print("Invalid value, please type a whole number. ")
    