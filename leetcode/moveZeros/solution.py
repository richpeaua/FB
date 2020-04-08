
def move_zeros(nums):
    back_i = back_pos = len(nums) - 1
    for i in nums:
        if nums[back_i] == 0:
            print(nums)
            nums[back_i], nums[back_pos] = nums[back_pos], nums[back_i]
            print(back_pos)
            back_pos -= 1 
        back_i -= 1

    print(nums)
                


num_list = [0,1,0,0,12]


move_zeros(num_list)