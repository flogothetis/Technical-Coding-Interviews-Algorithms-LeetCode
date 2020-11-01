'''
Palindrome LinkedList
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the
algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes
in the LinkedList.
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def middleOfList (head):
    slow, fast = head , head

    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow


def reverse(head):
  prev = None
  while (head is not None):
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def compareTwoLists(head1, head2):
    tmpHead1, tmpHead2 = head1, head2
    while (tmpHead1 is not None and tmpHead2 is not None):
        if  (tmpHead1.value != tmpHead2.value):
                return False
        tmpHead1 = tmpHead1.next
        tmpHead2 = tmpHead2.next
    if (tmpHead2 is None and tmpHead1 is None):
        return True
    return False

# Ο(N)
def is_palindromic_linked_list(head):
    middleNode = middleOfList(head)
    middleHead = reverse(middleNode)
    isPalindromic = compareTwoLists(head, middleHead)
    reverse(middleHead)
    return isPalindromic



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()







