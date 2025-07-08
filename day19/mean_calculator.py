
def mean_calculator(notes):
    """
    Calculate the average or the mean using a list of notes
    
    Arg:
    notes (list)
    
    return: 
    float - Mean of the notes
    """
    
    mean = sum(notes) / len(notes)
    
    #rounds our number 
    return round(mean, 2) 

print(mean_calculator([10, 4, 5, 9, 8]))
