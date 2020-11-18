'''
Missing number in array
Easy Accuracy: 29.81% Submissions: 6204 Points: 2
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N. Find the missing element.
'''


def missingNumber (array, N):
    num1 = 0
    for i in range (1, N+1):
        num1 ^= i
    num2 = 0
    for i in range (len(array)):
        num2 ^= array[i]
    return num1 ^ num2


print(missingNumber([1,2,3,4,5,6,7,8,10], 10))