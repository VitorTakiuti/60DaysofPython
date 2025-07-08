def count_words(text):
    """
    Count words in a string
    text: string
    return: number of words
    """
    #separate the wwords using the space in the text
    words = text.split()
    
    return len(words)

print(count_words("Hello there, how are you ?"))
