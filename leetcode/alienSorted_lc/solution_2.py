
# DONE Task 1 = dictionary with alien letters and their order/position value
# Task 2 = loop over words and char of each word
# Task 3 = perform a lookup for each char against alphabet_letter_position_value_dict
# Task 4 = perform comparison of char of a word against the char of the next word
# Task 5 = return results


def isAlienSorted(words, alien_alphabet):
    alien_alphabet_index = { letter: idx for idx, letter in enumerate(alien_alphabet) }

    for idx in range(len(words) - 1):
        word_1 = words[idx]
        word_2 = words[idx + 1]

        for char_idx in range(min(len(word_1), len(word_2))):
            word_1_char, word_2_char = word_1[char_idx], word_2[char_idx]
            if word_1_char != word_2_char:
                if alien_alphabet_index[word_1_char] > alien_alphabet_index[word_2_char]:
                    return False
                break
        else:
            if len(word_1) > len(word_2):
               return False
    return True


word_list = ["hello", "leetcode",]
alphabet = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(word_list, alphabet))
