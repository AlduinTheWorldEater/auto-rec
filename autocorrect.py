import data
import collector as clt

my_word = input("Enter the word: ")

corrections = clt.get_correct_words(my_word, data.prob_set, data.vocabulary)

for i, prob in enumerate(corrections):

    print(prob[0])
    if i == 2: break