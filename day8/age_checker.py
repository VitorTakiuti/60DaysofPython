#check the age of the user to see if he or she is allowed to drive

age = int(input("Type your age: "))

#In Brazil the age is 18+

if age >= 16:
    print("You can drive!")
else:
    print("You cannot Drive!")