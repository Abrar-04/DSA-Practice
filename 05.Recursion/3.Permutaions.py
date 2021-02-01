def getPermutations(arr):
    permutations=[]
    Helper(0,arr,permutations)

    return permutations

def Helper(i,arr,permutations):
    if i==len(arr)-1:
        permutations.append(arr[:])
    else:
        for j in range(i,len(arr)):
            swap(arr,i,j)
            Helper(i+1,arr,permutations)
            swap(arr,i,j)

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]


t=[1,2,3]
print(getPermutations(t))

