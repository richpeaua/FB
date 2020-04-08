import glob

input_files = glob.glob('input_files/*.txt')

for file in input_files:
    with open(file) as f:
        for line in f:
            print(line)