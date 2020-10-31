from collections import deque

# Time Complexity : O(N^3)
def subarraylessProductTarget ( array, target):
	windowStart = 0

	prod = 1
	result = []
	for windowEnd in range ( len(array)): # O(N^3)
		prod *= array[windowEnd]

		if ( prod >= target and windowStart <len(array)):
			prod/= array[windowStart]
			windowStart+=1

		temp_list = deque() # O(N) space 
		for i in range (windowEnd, windowStart-1, -1): # O(N^2)
			temp_list.appendleft(array[i])
			result.append(list(temp_list.copy())) # O(N)
	return result



def main():
  print(subarraylessProductTarget([2, 5, 3, 10], 30))
  print(subarraylessProductTarget([8, 2, 6, 5], 50))


main()
