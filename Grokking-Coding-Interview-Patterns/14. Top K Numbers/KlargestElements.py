'''
Problem Statement #

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
'''

from heapq import *

# Time Comp. O(KlogK + (N-K)logK)
# Space Comp. O(k)
def find_k_largest_numbers(nums, k):
  result = []
  min_heap = []

  for i in range (k):
      heappush(min_heap, nums[i])

  for i in range (k, len(nums)):
      if (min_heap[0] < nums[i]):
          heappop(min_heap)
          heappush(min_heap, nums[i])

  result = list(min_heap)
  return result


def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()

