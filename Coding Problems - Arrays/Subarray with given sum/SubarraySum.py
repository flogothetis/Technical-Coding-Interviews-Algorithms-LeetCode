#Subarray sum with positive elements
# Time Complexity : O(n)
# Space Complexity: O(1)

def subArraySum(array, sum):
	n = len (array)
	# if array is empty
	if(n==0):
		return  None

	if( min (array)<0):
		print('Cannot handle negative numbers')
		return None

	start_pos=0
	curr_sum= array[start_pos]
	for i in range (1,n):
		curr_sum+= array[i]
		if(curr_sum > sum):
			curr_sum-= array[start_pos]
			start_pos+=1

		if(curr_sum==sum):
			return [start_pos, i]

	return  None


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23

print (subArraySum(arr, sum) )