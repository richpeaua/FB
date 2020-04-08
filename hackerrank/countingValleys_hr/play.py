def countingValleys(n, s):
    valleyCount = 0
    mountainCount = 0
    elevation = 0
    prev_elevation = 0

    for step in s:
        prev_elevation = elevation
        if step == 'U':
            elevation += 1
        elif step == 'D':
            elevation -= 1

        if prev_elevation == 0 and elevation < 0:
            valleyCount += 1
        elif prev_elevation == 0 and elevation > 0:
            mountainCount += 1

    return valleyCount

steps = 'UDDDUDUU'
num_steps = 8

countingValleys(num_steps, steps)