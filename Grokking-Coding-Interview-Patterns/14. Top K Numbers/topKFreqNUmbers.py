'''
Problem Statement #

Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
'''
from heapq import  *

# Time Comp. O(N + NlogK)
# Space Comp. O(K)
def find_k_frequent_numbers(nums, k):
  freq = {}
  topNumbers = []
  for i in nums:
      freq[i] = freq.get(i,0) + 1

  min_heap=[]
  for num, frequency  in freq.items():
      heappush(min_heap, (frequency, num))
      if len(min_heap) > k :
          heappop(min_heap)


  for i in range (k):
      (frequency, num) = heappop(min_heap)
      topNumbers.append(num)


  return topNumbers


def main():

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()

