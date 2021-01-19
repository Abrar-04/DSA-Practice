def MoveElement(arr,ele):
    i=0
    j=len(arr)-1
    
    while i<j:
        while i<j and arr[j]==ele:
            j-=1
        if arr[i]==ele:
            arr[i],arr[j]=arr[j],arr[i]

        i+=1
    
    return arr


array1=[2,1,2,2,2,3,4,2]
element=2
print(MoveElement(array1,element))