# Time: O(n)
def checkSum(arr):
    arr_sum = sum(arr)
    if arr_sum % 2 != 0:
        return False

    sub_sum = arr_sum / 2
    i = current_sub_sum = 0

    while current_sub_sum < sub_sum:
        current_sub_sum += arr[i]
        i += 1
    if current_sub_sum == sub_sum:
        return [arr[:i], arr[i:]]
    else:
        return False

arr = [1, 50, 30, 5, 3, 2, 1, 90 ]

print(checkSum(arr))