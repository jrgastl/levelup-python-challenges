import secrets

def generate_passphrase(num_words, wordList_path='./text/diceware.wordlist.asc'):
    with open(wordList_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]
    return '  '.join(secrets.choice(word_list) for ii in range(num_words))

generate_passphrase(5)
