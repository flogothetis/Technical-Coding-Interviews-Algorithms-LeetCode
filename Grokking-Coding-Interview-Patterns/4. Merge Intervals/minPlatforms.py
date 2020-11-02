from heapq import *

from heapq import *

class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __lt__(self, other):
      return self.end < other.end

# Time Complexity :  O(NlogN)
def min_meeting_rooms(meetings):

    # sort all meetings
    meetings = sorted(meetings, key = lambda x: x.start)

    minPlatforms = 0
    minHeap = []

    for meetings in meetings:
        while (len(minHeap) > 0 and meetings.start >=minHeap[0].end):
            heappop(minHeap)
        heappush(minHeap, meetings)
        minPlatforms =  max (len(minHeap), minPlatforms)
    return minPlatforms


def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()
