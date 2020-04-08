def checkSum(arr):
    if sum(arr)%2 != 0: return False

    expected = sum(arr)/2
    i = curr = 0

    while curr < expected:
        curr += arr[i]
        i += 1

    return (arr[:i], arr[i:]) if curr == expected else False

arr = [1,2,3,4,5,6,21]

print(checkSum(arr))