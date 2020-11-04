'''
Find the Corrupt Pair (easy) #

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers
got duplicated which also resulted in one number going missing. Find both these numbers.
'''


# Time Complexity O(N)
def find_corrupt_numbers(num):

    i=0
    while (i < len(num)):
        j = num[i] - 1
        if (num[i]!=num[j]):
            num[i], num[j]= num[j], num[i]
        else:
            i+=1

    for i in range (len(num)):
        if (i+1 != num[i]):
            return [num[i], i+1]

    return [-1,-1]



def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()

