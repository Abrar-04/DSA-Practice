def SubarraySort(arr):
    minUnsorted=float('inf')
    maxUnsortted=float('-inf')

    for i in range(len(arr)):
        num=arr[i]
        if unOrdered(i,num,arr):
            minUnsorted=min(minUnsorted,num)
            maxUnsortted=max(maxUnsortted,num)

    if minUnsorted==float('inf'):
        return [-1,-1]
    
    isLessthan=0
    isGreatthan=len(arr)-1
    while minUnsorted > arr[isLessthan]:
        isLessthan+=1    
    while maxUnsortted < arr[isGreatthan]:
        isGreatthan-=1


    return [isLessthan,isGreatthan] 


def unOrdered(i,num,arr):
    if i==0:
        return num>arr[i+1]
    elif i==len(arr)-1:
        return num<arr[i-1]
    
    return num>arr[i+1] or num<arr[i-1]




array1=[1,2,4,7,10,11,7,12,6,7,16,18,19]
print(SubarraySort(array1))
    