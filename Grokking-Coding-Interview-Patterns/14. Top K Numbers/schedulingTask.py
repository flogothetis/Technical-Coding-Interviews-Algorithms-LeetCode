

from heapq import  *
from collections import  deque
def schedule_tasks(tasks, k):
  intervalCount = 0
  schedule_dict = {}
  schedule_q = deque()
  max_heap = []

  for task in tasks :
      schedule_dict[task] = schedule_dict.get(task,0) + 1

  for (task, freq) in schedule_dict.items():
      heappush(max_heap, (-freq, task))

  uncompleted_tasks = 0
  while (max_heap or  uncompleted_tasks !=0 ):
      if (max_heap):
        freq, task = heappop(max_heap)
        schedule_q.append((freq + 1, task))
        if (-freq - 1 >0):
            uncompleted_tasks +=1

        if (len(schedule_q) == k + 1):
            freq, task = schedule_q.popleft()
            if (-freq > 0):
                uncompleted_tasks-=1
                heappush(max_heap, (freq, task))
        intervalCount += 1
      else :
        intervalCount += ((k+1) - len(schedule_q))

        for i in range (len(schedule_q)):
            freq, task = schedule_q.popleft()

            if(-freq > 0):
                heappush(max_heap, (freq, task))
        uncompleted_tasks = 0


  return intervalCount


def main():
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
  print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()

