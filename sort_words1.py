import re

def sort_words(phrase):
    words = re.findall(r'[A-z]+', phrase)
    words.sort(key=str.casefold)
    finalString = " ".join(words)
    return finalString