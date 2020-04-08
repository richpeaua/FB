def isAlienSorted(words, order):
    order_index = {char: i for i, char in enumerate(order)}
    
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        
        for char_idx in range(min(len(word1), len(word2))):
            if word1[char_idx] != word2[char_idx]:
                if order_index[word1[char_idx]] > order_index[word2[char_idx]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False
            
    return True

word_list = ["hello"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(word_list, order))