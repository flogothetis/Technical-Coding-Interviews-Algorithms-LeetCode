'''
Find the Smallest Missing Positive Number (medium) #

Given an unsorted array containing numbers, find the smallest missing positive number in it.
'''


# Time Complexity : O(N)
def smallestMissingPositiveNumber(num):

    i=0
    while (i < len(num)):
        j = num[i] - 1
        if (num[i]>0 and num[i] <= len(num) and num[i]!=num[j]):
            num[i], num[j]= num[j], num[i]
        else:
            i+=1

    for i in range (len(num)):
        if (num[i] != i+1 ):
            return i+1
    return len(num) + 1



def main():
  print(smallestMissingPositiveNumber([-3, 1, 5, 4, 2]))
  print(smallestMissingPositiveNumber([3, -2, 0, 1, 2]))
  print(smallestMissingPositiveNumber([3, 2, 5, 1]))


main()
