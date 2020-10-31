'''
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
'''


def sqSorted (array):

	negativePointer = 0
	for i in range(len(array)):
		if (array[i] < 0):
			negativePointer = i

	nonNegativePointer  = negativePointer + 1
	result = []
	while (negativePointer>=0 and nonNegativePointer< len(array)):

		if (array[nonNegativePointer]**2 <= array [negativePointer]**2):
			result.append(array[nonNegativePointer]**2)
			nonNegativePointer+=1
		else:
			result.append(array[negativePointer]**2)
			negativePointer -=1

	print(len(result), negativePointer, nonNegativePointer)
	for i in range (negativePointer,-1,-1):
		result.append(array[negativePointer]**2)
	for i in range(nonNegativePointer, len(array)):
		result.append(array[nonNegativePointer]**2)

	return result


def main():

  print("Squares: " + str(sqSorted([-2, -1, 0, 2, 3])))
  print("Squares: " + str(sqSorted([-3, -1, 0, 1, 2])))


main()


