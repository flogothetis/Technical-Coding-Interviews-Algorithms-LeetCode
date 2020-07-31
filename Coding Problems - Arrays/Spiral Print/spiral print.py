def spiralPrint(array):
    # number of rows
    rows = len(array)
    # number of cols
    cols = len(array[0])

    offset = 0
    k = cols
    l = rows
    m = -1
    n = 0
    while (True):
        # print  from left -> right
        for i in range(offset, k):
            print(array[offset][i], end=' ')

        if (offset+1 <= l-1):
            # print right (top -> down )
            for i in range(offset + 1, l):
                print(array[i][k - 1], end=' ')
        else:
            break

        if k-2 >= m-1 :
            # print bottom (right -> left )
            for i in range(k - 2, m, -1):
                print(array[l - 1][i], end=' ')
        else:
            break

        if (l - 2 >= n-1):
            for i in range(l - 2, n, -1):
                print(array[i][offset], end=' ')
        else:
            break

        offset += 1
        k -= 1
        l -= 1
        m += 1
        n += 1


# Driver Code
a = [ [1, 2, 3, 4, 5, 6],
      [7, 8, 9, 10, 11, 12],
      [13, 14, 15, 16, 17, 18] ] 

spiralPrint(a)
