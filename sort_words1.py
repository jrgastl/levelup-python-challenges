'''
It was time to implement what I just learned in the exercise before. Also learned about the sort() method and key=str.casefold parameter.
Again, the instructor solution was more simple and showed me how to use the join() method.
'''

import re

def sort_words(phrase):
    words = re.findall(r'[A-z]+', phrase)
    words.sort(key=str.casefold)
    finalString = " ".join(words)
    return finalString
