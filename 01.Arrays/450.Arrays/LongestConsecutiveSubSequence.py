
def LongestConsecutiveSubSequence(arr):
    n=len(arr)
    temp=[]
    c=1
    maxLen=0

    arr.sort()

    for i in range(n):
        if arr[i] not in temp:
            temp.append(arr[i])


    x=len(temp)
    for i in range(x-1):
        if temp[i+1]-temp[i]==1:
            c+=1
        else:
            c=1
        maxLen=max(maxLen,c)
    return maxLen

arr = [ 2,6,1,9,4,5,3]
print(LongestConsecutiveSubSequence(arr))


