from heapq import *

class Item:
    def __init__(self, freq, num, timeSlot):
        self.freq = freq
        self.num = num
        self.timeSlot = timeSlot


    def __lt__(self, other):
        if (self.freq != other.freq):
            return self.freq > other.freq
        return self.timeSlot > other.timeSlot

# Time Comp : O(
class FrequencyStack:
  timeSlot  = 0
  max_heap = []
  freq_dict = {}

 # Time Comp : O(logN)
  def push(self, num):
    self.freq_dict[num] = self.freq_dict.get(num,0) +1
    heappush(self.max_heap, Item(self.freq_dict[num], num, self.timeSlot))
    self.timeSlot +=1

 #Time Comp: O(logN)
  def pop(self):
    item = heappop(self.max_heap)
    self.freq_dict[item.num]-=1

    if (self.freq_dict[item.num] == 0):
        del self.freq_dict[item.num]
    return item.num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()







