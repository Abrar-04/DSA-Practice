# pair wise 
def PowerSet(arr):
    subsets=[[]]
    
    for ele in arr:
        for i in range(len(subsets)):
            curSub=subsets[i]
            subsets.append(curSub+[ele])
    return subsets

# Recursive
# wrt to : last element is added to to every subset 
def powerset(arr,idx=None):
    if idx is None:
        idx=len(arr)-1
    elif idx <0:
        return [[]]

    ele=arr[idx]
    
    subsets=powerset(arr,idx-1)
    for i in range(len(subsets)):
        curSub=subsets[i]
        subsets.append(curSub+[ele])
    
    return subsets


arr1=[1,2,3]
print("Iter: ",PowerSet(arr1))
print("Recursive: ",powerset(arr1))
