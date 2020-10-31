'''
Minimum Window Sort (medium) #
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
'''

# Time Complexity O(N)
def maximumWindowSort (array):


	low =  0
	high = len(array)- 1

	if (low == high):
		return 0

	error = False
	while (low <= high):
		if (array[low+1] >= array[low]):
			low+=1
		else:
			error = True

		if(array[high-1]<= array[high]):
			high-=1
		else:
			error = True

		if (error):
			minElement = array[low]
			maxElement = array[low]
			for i in range (low, high+1):
				minElement  = min (minElement, array[i])
				maxElement  = max (maxElement, array[i])

			i = low -1
			while( i >=0 ):
				if (array[i] > minElement):
					low-=1
					i-=1
				else:
					break

			i = high +1
			while( i< len(array)):
				if( array[i]< maxElement):
					high+=1
					i+=1
				else:
					break
			return high - low +1
	return 0





def main():
  print(maximumWindowSort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(maximumWindowSort([1, 3, 2, 0, -1, 7, 10]))
  print(maximumWindowSort([1, 2, 3]))
  print(maximumWindowSort([3,2]))


main()
