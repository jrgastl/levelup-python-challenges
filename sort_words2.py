def sort_words(phrase):
    return ' '.join(sorted(phrase.split(), key=str.casefold))

print(sort_words('Text phrase Animals Fruits Vegetables'))