'''
Count the triplets
Easy Accuracy: 32.21% Submissions: 7249 Points: 2
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
'''


# Time Comp: O(N^2)
# Spoace Comp: O(1)
def countTriplets (array):
    array = sorted (array)

    counter = 0
    for i in range (len(array)-1 , 1, -1):
        low = 0
        high = i-1

        while (low < high ) :
            if ( array[low] +  array[high]  == array[i]):
                counter+=1
                low +=1
                high-=1

            elif (array[low] + array[high] < array[i]):
                low+=1
            else:
                high-=1

    return counter



arr = [1,2,2,2,3,3,4 ]
print (countTriplets(arr))