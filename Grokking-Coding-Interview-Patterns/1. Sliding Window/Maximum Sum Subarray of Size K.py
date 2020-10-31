'''''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum 
of any contiguous subarray of size ‘k’.
'''''

# Time Comlexity : O(N)
# Space Compexity: O(1)
def maximumSubArraySizeK (array, K):
    windowStart = 0
    globalMaxWindow = float ('-inf')
    windowSum = 0
    for i in range (len(array)):
        windowSum+= array[i]

        if (i >= K-1):
            globalMaxWindow = max(globalMaxWindow,windowSum)
            windowSum = windowSum - array[windowStart]
            windowStart+=1

    return globalMaxWindow

# Driver Code
input = [2, 1, 5, 1, 3, 2]
K=3
print(maximumSubArraySizeK(input,K))
