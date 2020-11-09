'''

'''

from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
      return  self.value < other.value


# Time Comp : O(NlogK)
def merge_lists(lists):
  resultHead = None
  min_heap = []
  # Append heads of the lists into a min heap
  for head in lists:
      if head is not None:
          heappush(min_heap, head)

  #Start creating the merged sorted list
  new_head  = new_tail = None

  while (min_heap):
      node = heappop(min_heap)

      if (new_head is None):
          new_head = node
          new_tail = node
      else:
          new_tail.next = node
          new_tail = new_tail.next

      if node.next is not None:
          heappush(min_heap, node.next)

  return new_head




def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

