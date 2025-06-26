def sort_words(phrase):
    return ' '.join(sorted(phrase.split(), key=str.casefold))