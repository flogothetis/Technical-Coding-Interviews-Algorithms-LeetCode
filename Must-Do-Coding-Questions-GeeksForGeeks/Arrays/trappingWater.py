'''
Trapping Rain Water
Medium Accuracy: 42.45% Submissions: 100k+ Points: 4
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
Structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.
'''

def trappingWater (array) :


    n = len(array)
    rightMaxBlock = [None] * n

    # Track right tollest block
    curr_max = -1
    for block in range (n-1, -1, -1):
        curr_max=  max(curr_max, array[block])
        rightMaxBlock[block] = curr_max


    left_curr_max = -1
    countTrappingWater = 0
    for block in range (n):
        left_curr_max = max (left_curr_max, array[block])
        countTrappingWater += max (min (left_curr_max, rightMaxBlock[block]) - array[block] , 0)
    return countTrappingWater

print( trappingWater([7 ,4 ,0 ,9]))
print( trappingWater([6,9,9]))

