# https://practice.geeksforgeeks.org/problems/sorted-matrix2333/1


def SortMatrix(arr,n):
    temp=[]
    k=0
    for i in range(0,n):
        for j in range(0,n):
            temp.append(arr[i][j])

    temp.sort()
    k=0

    for i in range(0,n):
        for j in range(0,n):
            arr[i][j]=temp[k]
            k+=1

    return arr

array=[ [10,15,20,30],
        [5, 8, 14,22],
        [12,13,18,19],
        [3, 4, 6,  9] ]

print(SortMatrix(array,4))
    