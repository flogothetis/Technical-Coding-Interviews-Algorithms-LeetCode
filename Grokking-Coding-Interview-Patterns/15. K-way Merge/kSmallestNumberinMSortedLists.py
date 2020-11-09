'''
Problem Statement #paiu
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Similar problems : Sorted Array + Median Element (K = N/2)

'''

from heapq import *
def find_Kth_smallest(lists, k):
  number = -1
  min_heap =[]
  # Push the first element of the arrays
  for i in range( len(lists)):
      heappush(min_heap, (lists[i][0], i, 0 ))
  # Extract the elements from min_heap until finding the k smallest element
  counter = 0
  val = -1
  while (min_heap):
      counter += 1
      val, row, col = heappop(min_heap)

      if ( col + 1 < len(lists[row])):
          heappush(min_heap, (lists[row][col+1], row, col+1))
      if(counter == k):
          break
  return val


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
