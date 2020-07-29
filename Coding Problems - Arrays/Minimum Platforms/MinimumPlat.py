# Program to find minimum
# number of platforms
# required on a railway
# station

# Returns minimum number
# of platforms required


# Time Complexity: O(NLogN + N)
# Space Complexity: O(1)
def findPlatform(arr, dep, n):
    globalPlat=1
    currPlat=1
    arr.sort()
    dep.sort()

    i=1
    j=0

    while i < n and j < n:
        if dep[j]< arr[i]:
            currPlat-=1
            j+=1
        elif arr[i] <= dep[j]:
            currPlat+=1
            i+=1

        if currPlat> globalPlat:
            globalPlat=currPlat
    return globalPlat

# driver code

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)

print("Minimum Number of Platforms Required = ",
      findPlatform(arr, dep, n))

# This code is contributed