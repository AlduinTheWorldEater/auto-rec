import string

def _split_words(word_str):
    return [(word_str[:i], word_str[i:]) for i in range(len(word_str))]

def Letter_delete(word_str):
    
    delete = []

    for i in range(len(word_str)):
        delete.append(word_str[:i] + word_str[i + 1:])

    return delete

def _Switch_letters(word_str):

    split_list = _split_words(word_str)
    switch_list = [a + b[1] + b[0] + b[2:] for a, b in split_list if len(b) >= 2]

    return switch_list

def _Replace_letters(word_str):

    split_list = _split_words(word_str)
    alphas = string.ascii_letters

    rep = [a + l + (b[1:] if len(b) > 1 else '') for a, b in split_list if b for l in alphas]

    return rep

def _Insert_letters(word_str):

    split_list = _split_words(word_str)
    alphas = string.ascii_letters

    inser = [a + l + b for a, b in split_list for l in alphas]

    return inser

