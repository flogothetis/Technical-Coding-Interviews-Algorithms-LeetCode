# Insertion Sort
# Time complexity: O(N^2)

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Move forward the elements to find the exact position of the key
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        # Put the key here
        array[j + 1] = key


arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i], end=' ')
