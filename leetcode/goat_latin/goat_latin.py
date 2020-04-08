#!/usr/bin/env python3

test_sentence = "I speak Goat Latin"

def goat_latinize_str(string):
    vowels = 'aeiou'

    goat_words = []

    for index, word in enumerate(string.split(" ")):
        index = index + 2
        suffix = "m" + ("a"*index) 
        if word[0].lower() in vowels:
            goat_words.append(word + suffix)
        else:
            goat_words.append(word[1:] + word[0] + suffix)

    return ' '.join(goat_words)

print(goat_latinize_str(test_sentence))