def TwoNumberSum (arr,sum):

    arr.sort()
    left=0
    right=len(arr)-1
    
    while (left < right):
        curSum=arr[left]+arr[right]
        
        if curSum==sum:
            return [arr[left],arr[right]]
        elif curSum<sum:
            left+=1
        elif curSum>sum:
            right-=1
        else :
            return None

    return []


array1=[3,5,-4,8,11,1,-1,6]
sum1=10
print(TwoNumberSum(array1,sum1))

