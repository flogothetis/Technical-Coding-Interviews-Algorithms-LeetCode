'''

Problem Statement #

Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

'''


from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


# Time Complexity O(N)
def reverse_sub_list(head, p, q):
  prev, next = head, head
  p_pointer, prev_p_pointer = None, None
  enable_reverse = False

  while next is not None :
      if next.value == p:
          prev_p_pointer = prev
          p_pointer = next
          enable_reverse= True
          prev = next
          next = next.next
          continue


      if (enable_reverse):
          next_step = next.next
          next.next = prev
          if (next.value == q):
              prev_p_pointer.next = next
              p_pointer.next = next_step
              break
          prev = next
          next = next_step
      else:
          prev= next
          next= next.next

  return head






def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
