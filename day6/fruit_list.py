#Fruit List

#fruits = ["banana", "apple", 'grape', 'pear', 'mango']
#for fruit in fruits:
    #print(fruit)
    
#now using input to create a list of fruits

fruits = []

while True:
    fruit = input("Choose the fruits that you want to list: ")
    if fruit == 'end':
        break
    fruits.append(fruit)
    
print(fruits)
