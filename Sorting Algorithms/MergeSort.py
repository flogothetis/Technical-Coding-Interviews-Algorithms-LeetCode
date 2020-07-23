import math


# Merge Sort Algorithm
# Total Compleity : O(NLogN) time
# Total Space: O(N) space from merge function

# Merge two sorted arrays, O(N)
def merge(leftArray, rightArray):
    leftArraySize = len(leftArray)
    rightArraySize = len(rightArray)

    leftPointer = 0
    rightPointer = 0

    # Write merging result into this list
    result = []

    while leftPointer < leftArraySize or rightPointer < rightArraySize:
        if leftPointer == leftArraySize:
            result.append(rightArray[rightPointer])
            rightPointer += 1
        elif rightPointer == rightArraySize:
            result.append(leftArray[leftPointer])
            leftPointer += 1
        else:
            if rightArray[rightPointer] < leftArray[leftPointer]:
                result.append(rightArray[rightPointer])
                rightPointer += 1
            else:
                result.append(leftArray[leftPointer])
                leftPointer += 1
    return result


def mergeSort(array):
    # Length of array
    if array is None:
        return

    n = len(array)
    if len(array) > 1:
        # Calcalte middle
        mid = int(math.floor(n // 2))
        leftArray = mergeSort(array[:mid])
        rightArray = mergeSort(array[mid:])
        result = merge(leftArray, rightArray)
        return result
    return array


# Driver code
a = [12, 11, 13, 5, 6, -8, 7]
print("Given array is")
print(*a)

a = mergeSort(a)

# Print output
print("Sorted array is : ")
print(*a)
