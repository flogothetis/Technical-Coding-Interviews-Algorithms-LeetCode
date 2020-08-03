from collections import deque

class Node :
    '''
    Class that represents the components of each node of the list
    '''
    def __init__(self,value):
        self.value=value
        self.next=None

class List:
    def __init__(self):
        self.head = None

    def append(self,value):
        '''
        Append elements to singly linked list
        :param value: the value of the new node
        '''
        newNode= Node(value)
        if(self.head is None):
            self.head=newNode
            return
        curr = self.head
        while(curr.next is not None):
            curr=curr.next
        curr.next=newNode

    def isPalindrome(self):
        '''
        :return: True if the list is palindrome, else False
        '''
        stack = deque()

        # Append elements of list into a stack (LIFO)
        curr=self.head
        while(curr is not None):
            stack.append(curr.value)
            curr=curr.next
        # Pop left from queue
        curr=self.head
        while (curr is not None):
            if(curr.value != stack.pop()):
                return  False
            curr=curr.next
        return True


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