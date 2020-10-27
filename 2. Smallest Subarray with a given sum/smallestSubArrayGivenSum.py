# Time Complexity: O(N + N)
#Space : O(1)
def smallestSubArrayOfSum(array, targetSum):
    windowStartPointer = 0
    windowEndPointer = 0
    curr_sum = 0;
    globalMinLength = len(array)
    while windowEndPointer < len(array):
        curr_sum += array[windowEndPointer]
        while curr_sum >= targetSum:
            globalMinLength = min(globalMinLength,
                                  windowEndPointer - windowStartPointer + 1)
            curr_sum -= array[windowStartPointer]
            windowStartPointer += 1
        windowEndPointer += 1
    return globalMinLength



# Driver Code
array = [2, 1, 5, 2, 3, 2]
S = 7
print(smallestSubArrayOfSum(array, S))