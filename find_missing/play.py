def find_missing_xor(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
        print(f'{num}: {xor_sum}')
    print('-'*5)
    for num in partial_set:
        xor_sum ^= num
        print(f'{num}: {xor_sum}')
    return xor_sum, '!'


test_arr1 = [4, 3, 7, 10, 1]

test_arr2 = [4, 1, 10, 7]

print(find_missing_xor(test_arr1, test_arr2))
