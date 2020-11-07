'''
Problem Statement #

Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference
with the given ‘key’.
'''

def search_min_diff_element(arr, key):
  return binarySearch(arr, key)

# Time Complexity: O(logN)
def binarySearch(arr, key):
    start, end = 0,len(arr)-1
    if (key>arr[end]):
        return arr[end]
    if (key <arr[0]):
        return arr[0]
    while (start <= end):
        mid = start + (end-start)//2
        if (arr[mid]== key):
            return arr[mid]
        elif (arr[mid]< key):
            start= mid+1
        else:
            end =mid -1

    # start == end +1
    if (arr[start] - key < key - arr[end]):
        return arr[start]
    return arr[end]

def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()
