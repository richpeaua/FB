def jumpingOnClouds(c):
    jump = index = 0
    while index < len(c) - 1:
        if index + 2 > len(c) -1 or c[index + 2] == 1:
            index += 1
        else:
            index += 2
        jump += 1
    return jump

    

count = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

print(jumpingOnClouds(count))
            