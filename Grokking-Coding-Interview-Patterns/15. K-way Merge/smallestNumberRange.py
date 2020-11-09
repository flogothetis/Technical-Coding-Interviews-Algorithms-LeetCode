from heapq import *
import math


# Time Complexity : NlogM
# N : total number of elements in arrays
# M : total different lists that existed in lists parameter
# Space Comp : O(M)
def find_smallest_range(lists):
    min_heap = []
    rangeStart, rangeEnd = 0 , math.inf

    # Push the first elements of the arrays into the min_heap
    maxElement = -math.inf
    for i in range (len(lists)):
        heappush(min_heap, (lists[i][0], i , 0))
        maxElement = max (maxElement, lists[i][0])
    while len(min_heap) == len(lists):
        val, row, col = heappop()
        if(rangeEnd - rangeStart > maxElement - val):
            rangeEnd = maxElement
            rangeStart = val
        if (col + 1 < len(lists[row])):
            heappush(min_heap, (lists[row][col+1], row, col + 1))
    return [rangeStart ,rangeEnd]

def main():
  print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
