# https://www.geeksforgeeks.org/rearrange-array-arri-arrj-even-arri/

def RearrangeEvenOdd(arr):
    n=len(arr)
    even=n//2
    odd=n-even
    temp=[0]*n

    for i in range(n):
        temp[i]=arr[i]
    
    temp.sort()

    #fill odd postions first
    j=odd-1
    for i in range(0,n,2):
        arr[i]=temp[j]
        j-=1
    
    #fill even postions
    j=odd
    for i in range(1,n,2):
        arr[i]=temp[j]
        j+=1

    return arr

arr=[1,2,3,4,5,6,7]
print(arr)
print(RearrangeEvenOdd(arr))
