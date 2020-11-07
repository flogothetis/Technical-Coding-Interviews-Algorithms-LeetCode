'''
Problem Statement #

Find the maximum value in a given Bitonic array.
An array is considered bitonic if it is monotonically increasing
and then monotonically decreasing. Monotonically increasing or
decreasing means that for any index i in the array arr[i] != arr[i+1].
'''




# Time Complexity : O(logN)
def find_max_in_bitonic_array(arr):
    start, end = 0,len(arr)-1

    if (arr[0] > arr[1]):
        return arr[0]
    if (arr[end-1] < arr[end]):
        return arr[end]

    while (start <= end):
        mid = start + (end-start)//2
        if (arr[mid-1] < arr[mid] > arr[mid+1]):
            return arr[mid]
        elif (arr[mid] < arr[mid+1]):
            start= mid+1
        else:
            end =mid -1

    return -1



def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()
