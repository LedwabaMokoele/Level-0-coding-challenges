def maximum(num_1,*nums):
    max = 0
    for num_i in nums:
        if(num_i > max):
            max = num_i
    if(num_1 > max):
        return num_1
    else:
        return max

max = maximum(4,7,32,27,22,96,1,3,32)
print(max)