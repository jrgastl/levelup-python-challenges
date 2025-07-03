def sort_words(phrase):
    return ' '.join(sorted(phrase.split(), key=str.casefold))


print(sort_words('It was time to implement what I just learned'))