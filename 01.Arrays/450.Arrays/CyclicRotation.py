# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1


def CyclicRotation(arr,d):
    n=len(arr)
    temp=[0 for i in range(n)]

    i=0
    r=d    
    while r<n:
        temp[i]=arr[r]
        i+=1
        r+=1
    
    r=0
    while r<d:
        temp[i]=arr[r]
        i+=1
        r+=1


    return temp

arr=[1,2,3,4,5,6,7]
print(CyclicRotation(arr,5))
