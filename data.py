import re
from collections import Counter

words = []

with open("./text_files/final.txt", "r") as file:

    file_data = file.read().lower()
    words = re.findall("\w+", file_data)

vocabulary = set(words)

def word_counts(word_set):

    word_counts = dict(Counter(word_set))
    return word_counts

def prob_words(word_count_dict):

    probabilities = {}
    word_sum = sum(word_count_dict.values())

    for i in word_count_dict:
        probabilities[i] = word_count_dict[i] / word_sum

    return probabilities

prob_set = prob_words(word_counts(vocabulary))