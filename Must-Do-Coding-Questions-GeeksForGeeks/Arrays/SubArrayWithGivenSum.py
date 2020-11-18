'''
Subarray with given sum
Easy Accuracy: 24.99% Submissions: 100k+ Points: 2
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
'''

# Time Comp : O(N)
# Space Comp : O(1)
def subArrayGivenSum (array, target):
    windowStart = 0
    sum = 0
    for windowEnd in range (len(array)):
        sum += array[windowEnd]


        while (sum > target):
            sum -= array[windowStart]
            windowStart+=1

        if (sum == target):
            return windowStart, windowEnd
    return -1,-1

# Time Comp : O(N)
# Space Comp : O(N)

def subArrrayGivenSumHandleNeg (array, target):
    map = {}

    curr_sum = 0
    for windowEnd in range (len(array)):

        curr_sum+= array[windowEnd]
        if (curr_sum == target) :
            return  0, windowEnd

        if (curr_sum - target  in map ):
            return  map[curr_sum- target] + 1 , windowEnd

        map[curr_sum] = windowEnd

    return -1, -1

print(subArrayGivenSum([1,2,3,7,5], 12))
print(subArrayGivenSum([1,2,3,4,5,6,7,8,9,10], 15))
print(subArrrayGivenSumHandleNeg([3,4,-2,-1], -3))