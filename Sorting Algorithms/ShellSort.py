def shellSort(array):
    n = len (array)
    gap = n // 2

    while gap > 0:
        j=gap
        while j<n:
            if array[j - gap]> array[j]:
                array[j-gap],array[j]=array[j],array[j-gap]
            j+=1
        gap=gap//2


# Driver code to test above
arr = [12, 34, 54, 2, 3]

n = len(arr)
print("Array before sorting:")
for i in range(n):
    print(arr[i]),

shellSort(arr)

print("\nArray after sorting:")
for i in range(n):
    print(arr[i]),