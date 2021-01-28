def maxOnes(arr):
    n=len(arr)#row
    m=len(arr[0])#col
    i=0
    j=m-1
    row=-1

    #we start off woth top right ele ,
    # if its 0: we go to next row,
    # if its 1: we go to adj left col, and store tht row for maxOne  
    while i<n and j>=0:
        if arr[i][j]==0:
            i+=1
        else:
            j-=1
            row=i

    return row

array= [[0,1,1,1],
        [0,0,1,1],
        [1,1,1,1],
        [0,0,0,0]]
    
print(maxOnes(array))