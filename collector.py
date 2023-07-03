import manipulator as mp
import data

def collector_type1(word, switches = True):

    collected_set = set()

    collected_set.update(mp.Letter_delete(word))
    collected_set.update(mp._Replace_letters(word))
    collected_set.update(mp._Insert_letters(word))

    if switches: collected_set.update(mp._Switch_letters(word))

    return collected_set

def collector_type2(word, switches = True):

    collected_set = set()

    primary_set = collector_type1(word, switches)

    for w in primary_set:
        if w: collected_set.update(collector_type1(w, switches))

    return collected_set

def get_correct_words(word, prob_dict, vocabulary):

    suggested_words = list((word in vocabulary and word) or (collector_type1(word).intersection(vocabulary)) or (collector_type2(word).intersection(vocabulary)))
    best_suggestions = [[s, prob_dict[s]] for s in reversed(suggested_words)]

    return best_suggestions

