# https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1

def Ksmall(arr,k):
    temp=[]
    n=len(arr)-1
    for i in range(0,n):
        for j in range(0,n):
            temp.append(arr[i][j])
    temp.sort()

    return temp[k-1]

arr1= [ [10,20,30,40],
        [15,25,35,45],
        [24,29,37,48],
        [32,33,39,50]]

print(Ksmall(arr1,7))

