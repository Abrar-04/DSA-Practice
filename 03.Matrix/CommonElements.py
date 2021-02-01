# https://www.geeksforgeeks.org/find-common-element-rows-row-wise-sorted-matrix/

def CommonElements(arr):
    m=len(arr)
    n=len(arr[0])
    col=[n-1]*m
    min_row=0

    while (col[min_row]>=0):

        for i in range(m):
            if ( arr[i][col[i]] < arr[min_row][col[min_row]]):
                min_row=i

        count=0

        for i in range(0,m):
            if (arr[i][col[i]]>arr[min_row][col[min_row]]):
                if (col[i]==0):
                    return -1 
                
                col[i]-=1

            else:
                count+=1
            
        if count==m:
            return arr[min_row][col[min_row]]

    return -1 


mat=[ [1,2,3,4,5],
      [2,4,5,8,10],
      [3,5,7,9,11],
      [1,3,5,7,9]]


print(CommonElements(mat))
