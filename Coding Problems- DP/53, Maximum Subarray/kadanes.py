from typing import List
def kadanes (list : List[int])->int :
	if (len(list) == 0 ):
		return 0

	global_sum = list[0]
	local_sum = list[0]

	for i in range (1, len(list)):
		local_sum = max (local_sum + list[i], list[i])
		global_sum = max(global_sum, local_sum)

	return global_sum



# Drive Code
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes(nums))