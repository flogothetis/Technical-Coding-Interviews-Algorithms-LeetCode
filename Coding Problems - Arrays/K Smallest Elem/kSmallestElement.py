# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
def partitioning(arr, l, h):
    pivot= arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]= arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1



# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
def kSmallestElement(arr, low, high, n, k ):
    if  k >=n :
        return  None
    if( low <=high):

        pos = partitioning(arr,low,high)
        if (pos +1 == k):
            return arr[pos]
        elif( pos+1 > k ):
            return kSmallestElement(arr,low, pos-1,n, k)
        else:
            return kSmallestElement(arr,pos+1, high, n, k)


# Driver Code
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 4;
    print("K'th smallest element is",
          kSmallestElement(arr, 0, n - 1, n, k))
