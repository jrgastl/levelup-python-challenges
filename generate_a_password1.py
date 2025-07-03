"""
Author Note:
I was really happy with this code and the optimizations that were done until I learned that the random module is not suitable for security purposes.s

Briefing:
Create a password generator that takes as input the number of words 
the password should have and generate a string of random words of 
the Diceware list separated by spaces as password.
>>> generate_passphrase(5):

    'vice fame tango abide verb' 
"""
import random
import re

def roll_dices():
    keyword = ''.join(str(random.randint(1, 6)) for _ in range(0,5))
    return keyword
          
def generate_passphrases(length):
    with open('./texts/diceware.wordlist.asc' ,'r', encoding='utf-8') as dicewareFile:
        dicewareWords = [line.split() for line in dicewareFile.readlines() if re.match(r'^[1-6]{5}\s', line)]
    dicewareDict = {words[0]:words[1] for words in dicewareWords}
    
    passphrase = ' '.join(dicewareDict[roll_dices()] for _ in range(length))
    print(passphrase)
            
generate_passphrases(5)