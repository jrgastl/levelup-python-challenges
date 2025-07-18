import re

def is_palindrome(text):
    clean_text = ''.join(re.findall(r'[a-z]+', text.lower()))
    reversed_text = clean_text[::-1]
    return clean_text == reversed_text

# Please, uncomment the line below to execute the code with the example given
# print(is_palindrome("Go hang a salami - I'm a lasagna hog."))