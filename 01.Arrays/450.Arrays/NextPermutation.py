def NextPermutation(arr):
    n=len(arr)-1
    idx=-1
    for i in range(n,0,-1):
        if arr[i]>arr[i-1] :
            idx=i
            break

    if idx==-1:
        arr.reverse()
    else:
        prev=idx
        
        for i in range(idx,n):
            if arr[i]>arr[idx-1] and arr[i]<a[prev]:
                prev=i
        
        arr[idx-1],arr[prev]=arr[prev],arr[idx-1]
        # reverse array from idx to n only
        arr[idx:arr[n]]=arr[idx:arr[n]][::-1]

    
    return arr

arr=[1,2,3]
print(NextPermutation(arr))