from Node import Node


class List:
    def __init__(self):
        self.head = None

    def mergeTwoSortedLists(self, headList1, headList2):
        '''
        Function that merge two lists that are both sorted.
        :param headList1: head of the first list
        :param headList2: head of the second list
        '''
        slowList1=headList1

        while headList1 is not None and headList2 is not  None:
            if headList1.value < headList2.value:
                slowList1=headList1
                headList1=headList1.bottom

            else:
                if slowList1 == self.head:
                    self.head= headList2
                    headList2 = headList2.bottom
                    self.head.bottom=slowList1
                    slowList1=self.head
                else:
                    slowListNext=slowList1.bottom
                    slowList1.bottom=headList2
                    headList2 = headList2.bottom
                    slowList1.bottom.bottom=slowListNext
                    slowList1=slowList1.bottom

        while(headList2 is not None):
            slowListNext = slowList1.bottom
            slowList1.bottom = headList2
            headList2 = headList2.bottom
            slowList1.bottom.bottom = slowListNext
            slowList1 = slowList1.bottom


    def flattening(self):
        '''
        Function that invokes 'mergeTwoSortedLists' to flatten a list of lists.
        Attention: Each list that from top to down must be sorted.
        '''
        if self.head is None :
            return
        curr= self.head
        currLeft = curr.left
        next=None
        while( currLeft is not None):
            next=currLeft.left
            self.mergeTwoSortedLists(curr, currLeft)
            curr.left=next
            currLeft=next



    def printList(self):
        '''
        Print entire list of lists
        '''
        leftPointer=self.head
        bottomPointer=self.head
        while leftPointer  is not None:
            while bottomPointer is not None:
                print(bottomPointer.value,' ->', end=' ')
                bottomPointer=bottomPointer.bottom
            leftPointer=leftPointer.left
            bottomPointer=leftPointer
            print("End")


    def buildList(self, listOfElem, numOfEachCol):
        '''
        Function to build a list of lists
        :param listOfElem: A 1d list that contains all the elements that will be inserted into the list of lists
        :param numOfEachCol: A 1d list that contains the number of elements that will be inserted in top-down
        lists
        '''
        if listOfElem == [] and numOfEachCol == []:
            return

        pos = 0
        bottomPointer = None
        leftPointer = None

        for k in numOfEachCol:
            for j in range (k):
                newNode = Node(listOfElem[pos])
                pos += 1
                if self.head is None:
                    self.head = newNode
                    bottomPointer = self.head
                    leftPointer = self.head
                elif j == 0:
                    leftPointer.left = newNode
                    leftPointer = newNode
                    bottomPointer = newNode
                else:
                    bottomPointer.bottom = newNode
                    bottomPointer = newNode


# Driver Code
mylist = List()
elementsOfList = [5, 7, 8, 30, 10, 20, 19, 22, 50, 28, 35, 40, 45]
numberOfElementsInEachCol = [4, 2, 3, 4]
mylist.buildList(elementsOfList, numberOfElementsInEachCol)
print("Initial list of lists")
mylist.printList()

mylist.flattening()
print("Final flattened list")
mylist.printList()

