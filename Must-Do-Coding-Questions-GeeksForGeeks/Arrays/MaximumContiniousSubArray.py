'''
Kadane's Algorithm
Medium Accuracy: 51.0% Submissions: 17890 Points: 4
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
'''
import math
def maximumContSubArray( array):

    globalMax = -math.inf
    curr_max = -math.inf
    for i in range(len(array)):
        curr_max = max (array[i], curr_max + array[i])
        globalMax = max(globalMax, curr_max)
    return globalMax


print(maximumContSubArray([-1, -2, -3, -4]))