def sort_words(phrase):
    return ' '.join(sorted(phrase.split(), key=str.casefold))

# Please, uncomment the line below to execute the code with the example given
# print(sort_words('Text phrase animals Fruits Vegetables'))