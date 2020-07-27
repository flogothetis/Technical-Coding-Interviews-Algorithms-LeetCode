# Merge two sorted arrays with O(1) extra space
# This script uses an alternative insertion sort algorithm
# to sort in-place two non-decreasing sorted algorithms
# Worst Case Time Complexity: O(n^2)
def merge(arr1, arr2):
    # Size of array 1
    n = len(arr1)
    # Size of array 2
    m = len(arr2)

    for i in range(1, n + m):
        if i < n:
            key = arr1[i]
        else:
            key = arr2[i - n]
        j = i - 1
        while j >= 0:
            if j == n - 1 and key < arr1[j]:
                arr2[j + 1 - n] = arr1[j]
            elif j < n and key < arr1[j]:
                arr1[j + 1] = arr1[j]
            elif j >= n and key < arr2[j - n]:
                arr2[j + 1 - n] = arr2[j - n]
            else:
                break
            j -= 1

        if j >= n:
            arr2[j + 1 - n] = key
        else:
            arr1[j + 1] = key


ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
# Size of array 1
n = len(ar1)
# Size of array 2
m = len(ar2)
merge(ar1, ar2)

print("After Merging \nFirst Array:", end="")
for i in range(n):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(m):
    print(ar2[i], " ", end="")
