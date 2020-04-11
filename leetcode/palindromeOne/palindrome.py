
#test_string = "A man, a plan, a canal: Panama"

test_inputs = {
    'test_string_pass1': "madam",
    'test_string_pass2': "`l;`` 1o1 ??;l`",
    'test_string_fail1': "tuple",
    'test_stringfail2': "I like Ham!",
}

def isPalindrome(string):
    potential_palindrome = ''.join(char for char in string if char.isalnum()).lower()
    if potential_palindrome == potential_palindrome[::-1]:
        return "is palindrome!"
    return "is not palindrome"


for case, test_string in test_inputs.items():
    print(isPalindrome(test_string))
    # Results = pass, pass, fail, fail 




