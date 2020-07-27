#Subarray sum with positive elements
# Time Complexity : O(n)
# Space Complexity: O(n), due to the hash map

def subArraySum(array, sum):
	n = len (array)
	# if array is empty
	if(n==0):
		return  None


	Map={}
	curr_sum= 0
	for i in range (0,n):
		curr_sum+= array[i]
		if curr_sum - sum in Map:
			return [Map[curr_sum-sum] +1, i]

		if curr_sum==sum:
			return [0, i]

		Map[curr_sum]= i

	return  None


# Driver program to test above function
if __name__ == "__main__":
	arr = [10, 2, -2, -20, 10]
	n = len(arr)
	Sum = -10

	print (subArraySum(arr, Sum))
