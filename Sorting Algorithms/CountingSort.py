import itertools


# Counting Sort

# Time complexity: O(n + k), where n is the total
# number of elements in array, and k is the largest element element
# in the array (+1).

# Space Complexity: 0(n+k)


def countingSort(array):
    # Find largest element in the array
    k = max(array)
    # Size of the array
    n = len(array)

    # Allocate auxiliary space for storing the amount of
    # occurances of the elements in array
    aux = [0] * (k + 1)

    for i in range(n):
        aux[array[i]] += 1

    # Cumulative Addition
    aux = list(itertools.accumulate(aux))

    # Allocate additional memory to re-arrange array's elements
    output = [0] * n
    for i in range(n):
        output[aux[array[i]] - 1] = array[i]

    # Copy output array to the original array
    array[:n] = output[:n]


# Driver code to test above

arr = [12, 34, 54, 2, 3]
countingSort(arr)
print(arr)
