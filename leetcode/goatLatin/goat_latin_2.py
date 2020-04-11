# DONE Task 1 = split out the words in the string and loop through
# DONE Task 2 = handle the words-begin-with-vowel case
# DONE Task 3 = handle words-begin-with-consonant case
# DONE Task 4 return goat latinized string

def goat_latinize_str(string):
    vowels = 'aeiou'

    goat_words = []
    
    for idx, word in enumerate(string.split(' ')):
        idx = idx + 1
        suffix = 'ma' + ('a' * idx)
        
        if word[0].lower() in vowels:
            goat_words.append(word + suffix)
        else:
            first_char = word[0]
            rest_of_word = word[1:]
            
            goat_words.append(rest_of_word + first_char + suffix)

    goat_latinized_string = ' '.join(goat_words)

    return goat_latinized_string
    
test_sentence = "I speak Goat Latin"
    
print(goat_latinize_str(test_sentence))
