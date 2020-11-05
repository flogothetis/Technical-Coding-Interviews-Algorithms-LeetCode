'''
Problem Statement #
Given an array of numbers and a number ‘k’, find the median of all the ‘k’
sized sub-arrays (or windows) of the array.
'''

from heapq import *
class SlidingWindowMedian:
  def __init__(self):
    self.min_heap =[]
    self.max_heap= []

  # Time Complexity: O(logN)
  def insert(self, num) :
    if ( not self.max_heap or num <= -self.max_heap[0]):
        heappush(self.max_heap, -num)
    else:
        heappush(self.min_heap, num)
  # Time Complexity: O(logN)
  def rebalance(self):
     if (len(self.max_heap) > len(self.min_heap) + 1):
         heappush(self.min_heap, -heappop(self.max_heap))
     elif (len(self.max_heap) < len(self.min_heap)):
         heappush(self.max_heap, -heappop(self.min_heap))
  # Time COomplexity: O(1)
  def getMedian(self):
      if (len(self.max_heap) == len(self.min_heap)):
          return (-self.max_heap[0] +  self.min_heap[0])/2
      else:
          return -self.max_heap[0]

  #Time Comp :O(K)
  #K : windowSize
  def reduceWindow(self, nums , windowStart):
      if (windowStart <0 or windowStart >len(nums)):
          return
      heap = None
      if (nums[windowStart] <= -self.max_heap[0]):
          heap = self.max_heap
          index = heap.index(-nums[windowStart])

      else:
          heap = self.min_heap
          index = heap.index(nums[windowStart])


      heap[index] = heap [-1]
      del heap[-1]
      heapify(heap)

  # Time Comp : O(N*K)
  def find_sliding_window_median(self, nums, k):
    result = []
    windowStart = 0
    for windowEnd in range (len(nums)):
        self.insert(nums[windowEnd])
        self.rebalance()
        if (windowEnd- windowStart + 1 == k):
            result.append(self.getMedian())
            self.reduceWindow(nums, windowStart)
            windowStart+=1
            self.rebalance()

    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
