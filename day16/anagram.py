def anagram(word):
    """
    Check if two words are anagrams or not
    word1: first word
    word2: second word
    return: True if those words are anagrams
    """
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    if sorted(word1) == sorted(word2):
        return f"Those words are anagrams"
    return f"those words aren't anagrams"


print(anagram("love", "vole"))