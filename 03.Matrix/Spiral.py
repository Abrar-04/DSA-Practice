def Spiral(arr):
    result=[]
    sr,sc=0,0
    er,ec=len(arr)-1,len(arr[0])-1

    while (sr<=er) and (sc<=ec):
        for col in range(sc,ec+1):
            result.append(arr[sr][col])
        for row in range(sr+1,er+1):
            result.append(arr[row][ec])
        for col in reversed(range(sc,ec)):
            result.append(arr[er][col])
        for row in reversed(range(sr+1,er)):
            result.append(arr[row][sc])

        sr+=1
        sc+=1
        er-=1
        ec-=1

    return result

array=[ [1 ,2 ,3 ,4],
        [5 ,6 ,7 ,8],
        [9,10,11 ,12],
        [13,14,15,16]]

print(Spiral(array))
# expected: 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10