from typing import  Dict, List


# Complexity O(totalCoins * total Amount), Space : O(1)
def coinChange (coinsList: List[int], totalAmount)->int:
	totalCoins = len(coinsList)
	if (totalCoins == 0 ):
		return  1

	#create dp table
	dp = [[0] * (totalAmount+1)] * 2
	#initialize dp table
	dp[0][0] = 1
	dp[1][0] = 1


	for i in range (1, totalCoins +1):
		for j in range (1, totalAmount +1):
			if (j-coinsList[i-1]) >=0:
				dp[i&1][j] = (dp[i&1 -1][j-coinsList[i-1]] + dp[i&1-1][j])
			else:
				dp[i&1][j] = dp[i&1-1][j]
	return dp[totalCoins&1][totalAmount]




#Driver Code

amount = 5
coins = [1, 2, 5]
print(coinChange(coins, amount))
