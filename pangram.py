def check_pangram(text):
    return 26 == len([x for x in set(list(text.lower())) if x.isalpha()])
