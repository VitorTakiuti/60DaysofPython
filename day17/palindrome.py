def palindrome(text):
    """
    Check if a number, text or word is a palindrome
    :stop text: word, text or number
    :return: A Message saying if it is or not 
    """
    text = str(text).replace(" ", "").lower()
    
    if text == text[::-1]:#invert the text
        return f"{text} is a palindrome"
    return f"{text} isn't a palindrome"

print(palindrome("lalala"))
print(palindrome("123321"))