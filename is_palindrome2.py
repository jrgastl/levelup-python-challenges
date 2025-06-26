import re

def is_palindrome(text):
    cleanText = ''.join(re.findall(r'[a-z]+', text.lower()))
    reversedText = cleanText[::-1]
    return cleanText

print(is_palindrome("Go hang a salami - I'm a lasagna hog."))