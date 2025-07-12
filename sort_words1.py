'''
Author Note:
I started this exercise right after checking the instructor solution for the exercise 2 (is_palindrome2.py), so the use of regular expressions was more or less automatic.
The instructor solution was more elegant in the end by using join() method to put everything together in one line.
'''

import re

def sort_words(phrase):
    words = re.findall(r'[A-z]+', phrase)
    words.sort(key=str.casefold)
    finalString = " ".join(words)
    print(finalString)

print(sort_words('Text phrase Animals Fruits Vegetables'))