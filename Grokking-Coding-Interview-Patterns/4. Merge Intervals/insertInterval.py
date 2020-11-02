'''
Problem Statement #
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position
and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
1. Non overlapping intervals
2. Add to appropriate position
3. Merge intervals from the new appended internal until the end of array
'''





def insert(intervals, new_interval):
   merged = []

   # Insert all non-overlaping intervals that are before new_interval
   i = 0
   while (intervals[i][0] < new_interval[0] and i< len(intervals)):
        merged.append([intervals[i][0], intervals[i][1]])
        i +=1

    # checK for union of intervals after new_interval
   start  = new_interval[0]
   end = new_interval[1]
   for j in range (i, len(intervals)):
       if intervals[j][0] <= end:
           end = max (end, intervals[j][1])
       else:
           merged.append([start, end])
           start = intervals[j][0]
           end = intervals[j][1]

   merged.append([start,end])
   return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()