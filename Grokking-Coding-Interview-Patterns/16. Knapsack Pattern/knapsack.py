'''
Problem Statement #
Given two integer arrays to represent weights and profits of ‘N’ items,
we need to find a subset of these items which will give us maximum profit su
ch that their cumulative weight is not more than a given number ‘C.’
Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
'''


def topDownKnapSack (W, productId, product_weights, product_values, memoization):
  if ((W,productId) in memoization):
    return memoization[(W,productId)]

  if W <=0 or productId < 0 :
    memoization[(W, productId)] = 0
    return  0

  selectProduct  = 0
  if ( W - product_weights[productId] >=0 ):
    selectProduct = topDownKnapSack(W-product_weights[productId], productId - 1, product_weights, product_values, memoization) +\
       product_values[productId]

  result = max (selectProduct, topDownKnapSack(W, productId-1, product_weights, product_values, memoization))
  memoization[(W, productId)] = result
  return  result




def bottomUpKnapSack (W, weights, profits):
  total_weights = W + 1
  total_profits = len (profits) + 1
  dp= [[0 for _ in range (total_weights)] for _ in range(total_profits)]

  for i in range (1, total_profits):
    for j in range (1, total_weights):
      if ( weights[i-1] <= j ):
        dp[i][j] = max (dp[i-1][j-weights[i-1]] + profits[i-1], dp[i-1][j])
      else:
        dp[i][j] = dp[i-1][j]
  return dp[total_profits-1][total_weights-1]

def solve_knapsack(profits, weights, capacity):

  #return topDownKnapSack (capacity, len(profits) -1, weights, profits, {})
  return bottomUpKnapSack (capacity, weights, profits)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()

