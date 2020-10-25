
from typing import Dict, List



#Time Complexity of Brute Force O(2^N)
#Time Complexity of DP : O(n)
def maxRobberProfit(moneyPerHouseList: List[int]):
	if(len(moneyPerHouseList) == 0):
		return 0;

	numberOfHouses = len(moneyPerHouseList)
	# create dp table
	dp = [None]* numberOfHouses
	dp[0] = moneyPerHouseList[0]
	if (len(moneyPerHouseList) == 1):
		return dp[0]
	dp[1] = max(moneyPerHouseList[0], moneyPerHouseList[1])
	for i in range(2,numberOfHouses):
		dp[i] = max (dp[i-1], moneyPerHouseList[i] + dp[i-2])

	return  dp[numberOfHouses-1]


# Time Complexity : O(n) / Space: O(1)
def maxRobberProfitEfficient(moneyPerHouseList: List[int]):
	if(len(moneyPerHouseList) == 0):
		return 0;

	numberOfHouses = len(moneyPerHouseList)
	# create dp table
	prev_prev_house = moneyPerHouseList[0]
	if(len(moneyPerHouseList) == 1):
		return prev_prev_house
	prev_house = max(moneyPerHouseList[0], moneyPerHouseList[1])
	if (len(moneyPerHouseList) ==2):
		return prev_house

	for i in range(2,numberOfHouses):
		current_house = max (prev_house, moneyPerHouseList[i] + prev_prev_house)
		prev_prev_house= prev_house
		prev_house = current_house

	return  current_house


# Driver code

monerPerHouseList  =  [5]
print(maxRobberProfit(monerPerHouseList))
