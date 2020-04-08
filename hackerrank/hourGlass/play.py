def hourGlassSum(arr):
    hg_highest_sum = 0
    hg_sums = []
    idx = 0
    sub_arr = 0
    hg_count = 0
    while hg_count < 16: 
        if sub_arr < 1 or idx == len(arr) - 1:
            sub_arr += 1
            idx = 0

        if 0 < idx < len(arr) - 1:
            hg_core = arr[sub_arr][idx]
            
            # position of top and bottom rows of hourglas
            l_idx, m_idx, r_idx = idx - 1, idx, idx + 1

            # sums of bottom and top hg rows 
            hg_top_sum = arr[sub_arr - 1][l_idx] + arr[sub_arr - 1][m_idx] + arr[sub_arr - 1][r_idx]
            hg_bottom_sum = arr[sub_arr + 1][l_idx] + arr[sub_arr + 1][m_idx] + arr[sub_arr + 1][r_idx]

            # sum of current hg
            hg_curr_sum = hg_bottom_sum + hg_top_sum + hg_core
            hg_sums.append(hg_curr_sum)

            if hg_count == 0:
                hg_highest_sum = hg_curr_sum
            elif hg_highest_sum < hg_curr_sum:
                hg_highest_sum = hg_curr_sum
            hg_count += 1
            
        idx += 1
    print(hg_sums)
    print(hg_highest_sum)

        



arr_2d = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

#[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
'''

hourGlassSum(arr_2d)
