
import math

def storeInplace(storePosition, array1, array2, maxNumber, value):
    if (storePosition < len(array1)):
        array1[storePosition] = (value)* maxNumber + array1[storePosition]
    else:
        array2[storePosition - len(array1)] = (value) *maxNumber + array2 [storePosition - len(array1)]


def mergeInPlace (array1, array2):

    maxNumber = max(max(array1), max(array2)) + 1

    storePosition = leftPointer = rightPointer = 0


    while (leftPointer < len(array1) and rightPointer < len(array2)):
        if (array1[leftPointer]%maxNumber <= array2[rightPointer]%maxNumber):
            storeInplace(storePosition, array1, array2, maxNumber, array1[leftPointer]%maxNumber )
            leftPointer+=1
        else:
            storeInplace(storePosition, array1, array2, maxNumber, array2[rightPointer] % maxNumber)
            rightPointer+=1
        storePosition+=1

    for i in range(leftPointer, len(array1)):
        storeInplace(storePosition, array1, array2, maxNumber, array1[i] % maxNumber)
        storePosition+=1
    for i in range(rightPointer, len(array2)):
        storeInplace(storePosition, array1, array2, maxNumber, array2[i] % maxNumber)
        storePosition+=1

    for i in range (len(array1)):
        array1[i] = array1[i]//maxNumber
    for j in range (len(array2)):
        array2[j] = array2[j]//maxNumber

array1 = [1,3,5,7]
array2 = [0,2,6,8,9]
mergeInPlace(array1, array2)
print(array1, array2)
