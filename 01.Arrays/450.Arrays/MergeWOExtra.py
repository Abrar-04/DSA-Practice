

def NaiveMerge(arr1,arr2):
    
    arr1.extend(arr2)
    arr1.sort()

    return arr1

arr1=[1,3,5,7]
arr2=[0,2,6,8,9]

print(NaiveMerge(arr1,arr2))



def MergeWOExtra(arr1,arr2):

    m=len(arr1)
    n=len(arr2)

    i=m-1
    j=0

    while i>0 and j<n :
        if arr1[i]>arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
        j+=1
        i-=1

    arr1.sort()
    arr2.sort()

    for x in arr1:
        print(x,end=" ")

    for x in arr2:
        print(x,end=" ")

    print()
    




arr1=[1,3,5,7]
arr2=[0,2,6,8,9]

print(MergeWOExtra(arr1,arr2))




