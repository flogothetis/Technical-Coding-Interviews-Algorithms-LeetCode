'''
Stock Buy Sell to Maximize Profit
Last Updated: 13-11-2020

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling
in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned
by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted
in decreasing order, then profit cannot be earned at all.
'''

def buyAndSell (array) :

    i = 0
    result = []
    while (i < len(array) - 1):

        # find local minima

        while (i < len(array) - 1  and array[i+1] <= array[i]):
            i += 1
        buy = i

        if (i == len(array) -1):
            break;

        i+=1
        while(i<len(array) and array[i]>= array[i-1]):
            i += 1
        sell = i - 1

        result.append((buy,sell))

    return result
# Driver code

# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]


# Fucntion call
print(buyAndSell(price))