def generator(s, n):
    return (n // len(s)) * s.count('a') + s[:n % len(s)].count('a')

# s = 'abc', a_count_in_s = 1, length_s = 3, n = (10 // 3) * a_count_in_s + a_count_in_s[:n % length]
# 'abcabcabcabca'

# if s = abc then a_count in s = 1


string = 'abc'
num = 10

print(generator(string, num))

