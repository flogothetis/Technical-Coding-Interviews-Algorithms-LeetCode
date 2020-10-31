'''
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous
subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

'''

# Time Complexity: O(N + N)
#Space : O(1)
def smallestSubArrayOfSum(array, targetSum):
    windowStartPointer = 0
    windowEndPointer = 0
    curr_sum = 0;
    globalMinLength = len(array) + 1
    while windowEndPointer < len(array):
        curr_sum += array[windowEndPointer]
        while curr_sum >= targetSum:
            globalMinLength = min(globalMinLength,
                                  windowEndPointer - windowStartPointer + 1)
            curr_sum -= array[windowStartPointer]
            windowStartPointer += 1
        windowEndPointer += 1
	if globalMinLength == len(array)+1:
		return 0
	return globalMinLength



# Driver Code
array = [2, 1, 5, 2, 3, 2]
S = 7
print(smallestSubArrayOfSum(array, S))