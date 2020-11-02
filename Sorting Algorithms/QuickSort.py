# Quick Sort
# Partitioning algorithm is adopted from CLRS book
# Time Complexity : Average Case O(NlogN)
# Space Complexity : In-place

def partioning (array, low, high ):
    pivot= array[high]
    #index to put the lowest values in the array
    i= low - 1
    for j in range(low, high):
        if(array[j]<pivot):
            i+=1
            array[j], array[i]= array[i],array[j]
    array[i+1],array[high]=  array[high],array[i+1]
    return i+1

def quickSort(array, low, high):
    if low < high :
        pi = partioning(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)

# Driver code to test abovehttps://www.youtube.com/watch?v=n6w9b41bG5s
arr= [ 3,2,0,123,1234,-1,3]

n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i], end =' ')