'''
Very helpful to discover the existence of regular expressions module with the instructor solution for this exercise.
'''

def is_palindrome(text):
    
    if type(text) != str:
        return False
    lowerText = text.lower()
    validChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
    cleanTextList = []
    for letter in lowerText:
        if letter in validChars:
            cleanTextList.append(letter)
    return cleanTextList == cleanTextList[::-1]

print(is_palindrome("Go hang a salami - I'm a lasagna hog."))
