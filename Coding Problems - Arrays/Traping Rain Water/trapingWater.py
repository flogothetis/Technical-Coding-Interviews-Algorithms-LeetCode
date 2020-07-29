def findWater(array):
    n=len(array)

    #max height of left bar of each cell
    left=[0]*n

    #max height of right bar of each cell
    right=[0]*n

    left[0]=array[0]
    for i in range (1,n):
        left[i]=max(left[i-1],array[i])

    right[n-1]=array[n-1]
    for i in range (n-2,-1,-1):
        right[i]=max(right[i+1],array[i])

    water=0
    for i in range(0,n):
        water+= min(left[i],right[i]) - array[i]
        if(min(left[i],right[i]) - array[i] < 0):
            print ('negative')

    return water


# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr))
