'''
Next Interval (hard) #

Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’ its
next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.
Write a function to return an array containing indices of the next interval of each input interval.
 If there is no next interval of a given interval, return -1. It is given that none of the intervals
  have the same start point.
'''

from heapq import  *
class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

# Time Complexity : O(NlogN)
# Space Complexiry : O(N)
def find_next_interval(intervals):
  result = []
  next_interval_heap = []
  current_interval_heap =[]

  for idx in range (len(intervals)):
      heappush(current_interval_heap, (intervals[idx].end, intervals[idx].start, idx))
      heappush(next_interval_heap, (intervals[idx].start, intervals[idx].end, idx))

  for _ in range (len(intervals)):
      curr_end, curr_start, curr_idx = heappop(current_interval_heap)
      next_idx = -1
      while (next_interval_heap and next_interval_heap[0][0]< curr_end):
        heappop(next_interval_heap)
      if(next_interval_heap):
        next_start, next_end, next_idx = heappop(next_interval_heap)
      result.append(next_idx)
  return result



def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()
