The rules of Goat Latin are as follows:

1. If a word begins with a consonant (i.e. not a vowel), remove the first
    letter and append it to the end, then add 'ma'.
    For example, the word 'goat' becomes 'oatgma'.

2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word.
    For example, the word 'I' becomes 'Ima'.

3. Add one letter "a" to the end of each word per its word index in the
    sentence, starting with 1. That is, the first word gets "a" added to the
    end, the second word gets "aa" added to the end, the third word in the
    sentence gets "aaa" added to the end, and so on.

Write a function that, given a string of words making up one sentence, returns
that sentence in Goat Latin. For example:
ps
  string_to_goat_latin('I speak Goat Latin')

would return: 'Ima peaksmaa oatGmaaa atinLmaaaaa'  
