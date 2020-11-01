from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()




def middleOfLinkedList(head):
	slow, fast = head, head

	while (fast is not None and fast.next is not None):
		slow = slow.next
		fast= fast.next.next
	return slow

def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def reorder (head):

	firstHalfHead = head
	secondHalfHead = reverse(middleOfLinkedList(head))

	while (firstHalfHead is not None and secondHalfHead is not None):
		nextOfFirstHalf = firstHalfHead.next
		nextOfSecondHalf = secondHalfHead.next

		firstHalfHead.next = secondHalfHead
		secondHalfHead.next = nextOfFirstHalf
		secondHalfHead = nextOfSecondHalf
		if(firstHalfHead.next is not None):
			firstHalfHead = firstHalfHead.next.next

	if (firstHalfHead.next is not None):
		firstHalfHead.next = None


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  head.next.next.next.next.next.next = Node(19)
  reorder(head)
  head.print_list()


main()



