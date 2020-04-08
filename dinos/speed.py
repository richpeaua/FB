import math
import collections

def bipedal_dino_speed_sorter(dataset1, dataset2):
    bipedal_dinos = {} # { dino_name: speed }
    g = 9.8

    with open(dataset1) as f:
        for line in f.readlines()[1:]:
            dino_name, stride_len, stance = line.strip().split(",")
            
            if stance == 'bipedal':
                bipedal_dinos[dino_name] = float(stride_len)

    with open(dataset2) as f:
        for line in f.readlines()[1:]:
            dino_name, leg_len, diet = line.strip().split(',')
        
            if dino_name in bipedal_dinos:
                leg_len, stride_len = float(leg_len), bipedal_dinos[dino_name]
                
                speed = ((stride_len/leg_len) - 1) * math.sqrt(leg_len*g)
                
                bipedal_dinos[dino_name] = speed
            #TODO: remove dinos not in both datasets

    with open('bipedal_dinos.txt', 'w') as open_file:
        open_file.write('NAME, SPEED\n')
        for dinos, speed in sorted(bipedal_dinos.items(), key=lambda x: x[1], reverse=True):
            open_file.write(f'{dinos}, {speed}\n')



bipedal_dino_speed_sorter('dataset2.csv', 'dataset1.csv')
            