from typing import List, Tuple

def getFirstDimension(item )->int:
	return item[0]

def LIS (dollSizes:List[List[int]])->int :
	n = len(dollSizes)
	#create DP table
	dp= [1]*n

	global_max = 1
	for i in range  (1,n):
		for j in range(i):
			if(dollSizes[j][0] < dollSizes[i][0] and
					   dollSizes[j][1] < dollSizes[i][1]):
				dp[i]= max (dp[i], dp[j] + 1)
				global_max = max(global_max, dp[i])

	return  global_max

def longestEnvelope(dollSizes:List[Tuple[int,int]])->int:
	# sort according to the first dimension
	dollSizes = sorted(dollSizes, key=getFirstDimension)
	print (dollSizes)
	return  LIS(dollSizes)



#Driver code

dollSizes = [[5,4],[6,4],[6,7],[2,3]]
print(longestEnvelope(dollSizes))





