'''
Problem Statement #\
We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1
to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just
before the object with sequence number ‘4’.  Write a function to sort the objects in-place on their creation
sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer
array containing only the sequence numbers, though each number is actually an object.

'''

def cycleSort (array):
    pointer = 0

    while (pointer < len(array)):
        while (array[pointer] != pointer+1):
            j = array[pointer]
            array[pointer], array[j-1]= array[j-1], array[pointer]
        pointer+=1

    return array
def main():
  print(cycleSort([3, 1, 5, 4, 2]))
  print(cycleSort([2, 6, 4, 3, 1, 5]))
  print(cycleSort([1, 5, 6, 4, 3, 2]))


main()
