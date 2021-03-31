# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

#O(n^2)
def CountInversion(arr):
    inv_count=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                inv_count+=1
    return inv_count

arr=[8,4,2,1]
print(CountInversion(arr))

#O(nlogn)
# use a merge sort type approach
    
def mergeSort(arr):
    n=len(arr)
    temp=[0]*n #a temp arr created with 0

    return _mergeSort(arr,temp,0,n-1)

def _mergeSort(arr,temp,left,right):
    inv_count=0 # stores the count 

    if left<right: #if ele exists
        mid=(left+right)//2

        inv_count+=_mergeSort(arr,temp,left,mid) #left subarr
        inv_count+=_mergeSort(arr,temp,mid+1,right) #right subarr

        inv_count+=merge(arr,temp,left,mid,right) #merge both subarr in sorted manner

    return inv_count

def merge(arr,temp,left,mid,right):
    i=left #start of left subarr
    j=mid+1 # start of right subarr
    k=left # start of new sorted arr
    inv_count=0

    while i<=mid and j<=right: # ele exists and not overflown

        if arr[i]<=arr[j]: # no inversion as they are sorted  
            temp[k]=arr[i]
            k+=1
            i+=1
        else: # inversion occurs 
            temp[k]=arr[j]
            inv_count+=(mid-i+1) # no.of inversions
            k+=1
            j+=1
    
    while i<=mid: # copy remaining elements of left subarr
        temp[k]=arr[i]
        k+=1
        i+=1
    while j<=right: # copy rem elements of right subarr
        temp[k]=arr[j]
        k+=1
        j+=1

    for x in range(left,right+1): # copy temp arr into arr
        arr[x]=temp[x]

    return inv_count

    


print("optimized")
arr1=[8,4,2,1]
print(mergeSort(arr1))