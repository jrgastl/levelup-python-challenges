'''
Input: path to a text file
Output: print message with:
    - total number of words
    - top 20 most frequent words
    - top 20 words ocurrence

Example:
>>> count_words('input.txt')

    Total Words: 473

    Top 20 Words:
    TEXT        13
    CHALLENGE   11
    WORDS       9
    YOUR        5
    FUNCTION    5

Words contain:
    -Letters
    -Numbers
    -Apostrophes
    -Hyphens
'''
import re

def count_words(file_path):
    with  open(file_path, 'r', encoding='UTF-8') as file:
        all_words = re.findall(r"[A-Za-z0-9-']+", file.read())
        all_words = [word.upper() for word in all_words]
    wordsOcurrence = {}
    for word in all_words:
        wordsOcurrence[word] = wordsOcurrence.get(word,0) + 1
    ocurrencesList = sorted(list(wordsOcurrence.values()),reverse=True)
    top20 = [(word,ocurrence) for ocurrence in ocurrencesList[0:20] for word in wordsOcurrence if wordsOcurrence[word] == ocurrence]
    print(f'\nTotal Words: {len(all_words)}\n\nTop 20 Words:\n')
    for place in top20:
        print(f'{place[0]}\t{place[1]}')

count_words('./texts/pg100.txt')