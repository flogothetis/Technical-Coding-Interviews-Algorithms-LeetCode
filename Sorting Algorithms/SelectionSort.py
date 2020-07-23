#Selection Sort Algorithm
#Time Complexity : O(N^2)
def selectionSort(array):
    n =len(array)
    for i in range (n):
        min=array[i]
        min_pos=i
        for j in range (i+1,n):
            if(array[j]< min):
                min=array[j]
                min_pos=j

        #Substitute the value of i-th position
        #with the minimum value
        temp=array[i]
        array[i]= array[min_pos]
        array[min_pos]=temp


arr = [12, 11, 13, 5, 6]
selectionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i],end =' ')