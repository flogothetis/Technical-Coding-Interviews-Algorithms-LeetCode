from collections import deque

class Node :
    '''
    Class that represents the components of each node of the list
    '''
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    left=None

    def __init__(self):
        self.head = None

    def append(self,value):
        '''
        Append elements to singly linked list
        :param value: the value of the new node
        '''
        newNode= Node(value)
        if self.head is None:
            self.head=newNode
            return
        curr = self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=newNode

    def isPalindromeUtil(self, rightNode):
        left = rightNode

        if(rightNode is None):
            return True

        ans = self.isPalindromeUtil(rightNode.next)
        if ans:
            return True



    def isPalindrome(self):
        return self.isPalindromeUtil(self.head)


# Driver Code
list = List()
list.append(0)
list.append(1)
list.append(2)
list.append(3)
list.append(2)
list.append(1)
list.append(0)
print("Is my list palindrome ?")
print(list.isPalindrome())