def ZigzagTraverse(arr):
    ht=len(arr)-1
    wt=len(arr[0])-1
    result=[]
    row,col=0,0
    goDown=True

    while not isOutofBounds(row,col,ht,wt):
        result.append(arr[row][col])

        if goDown:#executes when we want to go down            
            if col==0 or row==ht:
                goDown=False#once we go down, we want to go up in next chance so we set to false  
                if row==ht:
                    col+=1 #left2right
                else:
                    row+=1 #top2bottom
            else:#diagonalDownwards
                row+=1
                col-=1


        else:#executes when we want to go up
            if row==0 or col==wt:
                goDown=True#once we go up, we want to go down in next chance so we set to true
                if col==wt:
                    row+=1#top2bottom
                else:
                    col+=1#left2right
            else:#diagonalUpwards
                row-=1
                col+=1

    return result

def isOutofBounds(row,col,ht,wt):
    return row<0  or row>ht or col<0 or col>wt


array1=[[1,3,4,10],
        [2,5,9,11],
        [6,8,12,15],
        [7,13,14,16]
        ]
print(ZigzagTraverse(array1))