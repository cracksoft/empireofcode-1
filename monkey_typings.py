def count_words(text, words):
    return sum(text.lower().count(x) > 0 for x in words)
