def coinChange(array, value):
    n = len(array)
    if (value == 0 or n == 0):
        return 0
    dp = [0] * (value + 1)

    for i in range(1, value + 1):
        for j in range(n):
            if (array[j] > i):
                continue
            if dp[i % array[j]] != 0 or (dp[i % array[j]] == 0 and i % array[j] == 0):
                print(i, j)
                dp[i] += (1 + dp[i % array[j]] + ((i//array[j]-1)*dp[i//array[j]]))
                
    print(dp)
    return dp[value]


if __name__ == '__main__':
    array = [2, 5, 3, 6]
    change_value = 10
    print(coinChange(array, change_value))

