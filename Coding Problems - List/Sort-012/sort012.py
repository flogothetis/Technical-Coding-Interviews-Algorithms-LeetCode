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

    def printList (self):
        '''
        Prints the contents of the list in terminal
        '''
        curr = self.head
        while( curr is not None):
            print ( curr.value, end=' ')
            curr=curr.next
        print()
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

    def sort012 (self) :
        '''
        Sort a list of 0,1 and 2s
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        curr = self.head
        # list of counters of 0,1 and 2s
        counters = [0,0,0]
        while curr is not None:
            counters[curr.value]+=1
            curr=curr.next
        # Now traverse the list and substitute the first nodes of the list
        # with zeros (totally, counter[0] zeros). The same algorithm is followed
        #  for 1s and 2s.
        curr = self.head
        for i in range (len(counters)):
            for j in range (counters[i]):
                curr.value=i
                curr=curr.next






# Driver Code
list = List()
list.append(0)
list.append(1)
list.append(2)
list.append(0)
list.append(2)
list.append(1)
list.append(0)
print ('List before sorting')
list.printList()
print('List after sorting')
list.sort012()
list.printList()