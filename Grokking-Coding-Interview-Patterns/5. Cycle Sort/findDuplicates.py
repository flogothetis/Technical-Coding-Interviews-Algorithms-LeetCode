'''
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times. Find that duplicate number
without using any extra space. You are, however, allowed to modify the input array.
'''


# Time Complexity : O(N)
def findTheDuplicates(num):

    i=0
    while (i < len(num)):
        j = num[i] - 1
        if (num[i]!=num[j]):
            num[i], num[j]= num[j], num[i]
        else:
            i+=1

    dupl_l = []
    for i in range (len(num)):
        if (i+1 != num[i]):
            dupl_l.append(num[i])
    return dupl_l




def main():
  print(findTheDuplicates([3, 4, 4, 5, 5]))
  print(findTheDuplicates([5, 4, 7, 2, 3, 5, 3]))


main()
