def SpiralTravers(arr):
    result=[]
    SR=0
    SC=0
    ER=len(arr)-1
    EC=len(arr[0])-1

    while (SR<=ER) and (SC<=EC):

        for col in range(SC,EC+1):
            result.append(arr[SR][col])

        for row in range(SR+1,ER+1):
            result.append(arr[row][EC])

        for col in reversed(range(SC,EC)):
            result.append(arr[ER][col])

        for row in reversed(range(SR+1,ER)):
            result.append(arr[row][SC])

        SR+=1
        SC+=1
        ER-=1
        EC-=1

    return result

array1=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
print(SpiralTravers(array1))


'''
           SC       EC
           |        | 
    SR --[ 1, 2, 3, 4]
         [12,13,14, 5]
         [ 11,16,15,6]
    ER --[ 10,9, 8, 7]

    # outer boundary
    first row is traversed : sc,ec+1     ==  [SR][col]        -> 1,2,3,4
    last col is traversd   : sr+1,er+1   ==  [row][EC]        -> 5,6,7
    last row is traversed  : reversed (sc,ec) == [ER][col]    -> 8,9,10
    first col is traversed : reversed (sr+1,er) == [row][SC]  -> 11,12

    #inner boundary
    increment pointers

'''