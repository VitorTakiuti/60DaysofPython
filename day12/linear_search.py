def linear_search(list, searched_number):
    """
    Search for a number in a Linear_search
    
    :stop list: numbers list
    :stop searched_number: search number
    """
    
    for i, number in enumerate(list): #passa por cada ite de uma lista e os contabiliza
        if number == searched_number: 
            return i 
    
    return -1
        
list = [10,2,4,6,7,8,11]
searched_number = 7

searching_number = linear_search(list, searched_number)
print(searching_number)

if searching_number != -1:
    print(f"The number found at position: {searching_number}" )
else: 
    print("Number not found!")