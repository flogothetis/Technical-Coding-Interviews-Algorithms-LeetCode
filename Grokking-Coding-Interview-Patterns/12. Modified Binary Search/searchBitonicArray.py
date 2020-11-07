'''
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic
if it is monotonically increasing and then monotonically decreasing. Monotonically increasing
or decreasing means that for any index i in the array arr[i] != arr[i+1].
Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
'''

# Time Complexity : O(logN)
def find_max_in_bitonic_array(arr):
    start, end = 0,len(arr)-1

    if (arr[0] > arr[1]):
        return 0
    if (arr[end-1] < arr[end]):
        return end

    while (start <= end):
        mid = start + (end-start)//2
        if (arr[mid-1] < arr[mid] > arr[mid+1]):
            return mid
        elif (arr[mid] < arr[mid+1]):
            start= mid+1
        else:
            end =mid -1

    return -1

# Time Compl : O(logN)
def modifiedBS (start, end, arr, isAscedingOrder, key):

    start, end = 0, len(arr) -1

    while (start <= end):
        mid  = start + (end- start)//2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] < key and isAscedingOrder):
            if (isAscedingOrder):
                start = mid +1
            else:
                end = mid - 1
        else:
            if(isAscedingOrder):
                end = mid -1
            else:
                start = mid +1
    return -1

# Time Comp : O(logN)
def search_bitonic_array(arr, key):
  peak =  find_max_in_bitonic_array(arr)
  if (peak == - 1):
      print("Something got wrong")
  if(key == arr[peak]):
      return peak
  elif (key < arr[peak]):
      return modifiedBS(0, peak - 1, arr,  True, key)
  else:
      return  modifiedBS(peak+1, len(arr)-1, False, key)


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()
