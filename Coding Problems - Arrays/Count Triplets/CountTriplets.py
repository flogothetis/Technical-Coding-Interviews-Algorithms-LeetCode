def countTriplets(array):
    if array is None:
        return 0

    if len(array) == 0:
        return 0
    # Find max Value
    maxValue = max(array)
    # Count frequency of each positive integer
    freq = [0] * (maxValue+1)

    for i in range(len(array)):
        freq[array[i]] += 1

    ans = 0
    # Case 1: Count 0,0,0
    ans += freq[0] * (freq[0] - 1) * (freq[0] - 2) // 6

    # Case 2: Count x,0,x

    for x in range(1, len(freq)):
        ans += freq[0] * freq[x] * (freq[x] - 1) // 2

    # Case 0, x+x,2x

    for x in range(1, len(freq) // 2):
        ans += freq[2 * x] * (freq[x] * (freq[x] - 1)// 2)

    # Case x,y,x+y

    for x in range(1, len(freq)):
        for y in range(x + 1, len(freq) - x):
            ans += freq[x] * freq[y] * freq[x + y]

    return ans


# Driver code
arr = [ 1, 2, 3, 4, 5]

print(countTriplets(arr))