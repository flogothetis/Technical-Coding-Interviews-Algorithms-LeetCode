
def minJumps(array):
    n = len(array)
    #Define dp table
    dp = [float('inf')]*n
    dp[0]=0

    for i in range (1, n):
        for j in range (i):
            if (i-j) <= array[j] and (dp[j] != float('inf')):
                dp[i] = min(dp[i], 1+ dp[j])
    return dp[n-1]

if __name__ == '__main__':
    array = [1, 3, 6, 1, 0, 9]
    print(minJumps(array))
