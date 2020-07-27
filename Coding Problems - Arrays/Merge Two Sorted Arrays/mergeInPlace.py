# Merge two sorted arrays with O(1) extra space
# and O(n+m) time complexity


def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    # Find max value of both arrays
    maxValue = max(max(arr1), max(arr2)) + 1
    i = 0
    j = 0
    pointer = 0
    while i < n and j < m:
        if arr1[i] % maxValue > arr2[j] % maxValue:
            if pointer < n:
                arr1[pointer] = arr1[pointer] + (arr2[j] % maxValue) * maxValue

            else:
                arr2[pointer - n] = arr2[pointer - n] + (arr2[j] % maxValue) * maxValue
            pointer += 1
            j += 1
        else:
            if pointer >= n:
                arr2[pointer - n] = arr2[pointer - n] + (arr1[i] % maxValue) * maxValue
            else:
                arr1[pointer] = arr1[pointer] + (arr1[i] % maxValue) * maxValue

            pointer += 1
            i += 1

    for x in range(i, n):
        arr2[pointer - n] = arr2[pointer - n] + (arr1[x] % maxValue) * maxValue
        pointer += 1

    for x in range(j, m):
        arr2[pointer - n] = arr2[pointer - n] + (arr2[x] % maxValue) * maxValue
        pointer += 1

    for i in range(n):
        arr1[i]= arr1[i] // maxValue
    for j in range(m):
        arr2[j]=arr2[j] // maxValue


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
