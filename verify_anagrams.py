def verify_anagrams(first_word, second_word):
    return (''.join(sorted(first_word.lower())).strip()) == (''.join(sorted(second_word.lower())).strip())
