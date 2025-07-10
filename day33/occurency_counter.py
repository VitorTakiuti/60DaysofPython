from collections import Counter

def occurency_counter():
    """
    This Function will count the number of occurencies of a element in a list
    
    Arg: 
    List of elements
    
    return:
    Counter 
    """
    
    count = Counter(list)
    
    for element, quantity in count.items():
        print(f"{element}: {quantity}")
        
    return "The Counter was sucessfully done!"
    
if __name__ == "__main__":
    list_exemple = ['banana', 'grape', 'orange', 'banana', 'grape', 'orange', 'pear', 'apple']
    
    print(occurency_counter(list_exemple))