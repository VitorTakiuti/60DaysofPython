#A Prime number is only divided by 1 and itself
number = int(input("Type a number to see if its prime or not: "))

is_primenumber = True

if number <= 1:
    is_primenumber = False
    
for i in range(2, int(number ** o.5) + 1):
    if number % i == 0:
        is_primenumber = False
        break
    
if is_primenumber:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
    