'''
Largest Number formed from an Array
Medium Accuracy: 29.19% Submissions: 2899 Points: 4
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
The result is going to be very large, hence return the result in the form of a string.
'''
from functools import cmp_to_key

def compare (num1, num2) :
    num1num2 = int(str(num1) + str(num2))
    num2num1 = int(str(num2) + str(num1))


    print(num1, num2, num1num2, num2num1)

    if ( num1num2 < num2num1) :
        return -1
    elif (num1num2 == num2num1) :
        return 0
    else:
        return 1


def largestNumber (array) :
    array = sorted(array, reverse=True, key=cmp_to_key(compare))
    return "".join([ str(i) for  i in array])



#Driver Code
print(largestNumber([54, 546, 548, 60]))

