def ThreeNumSum(arr,target):
    arr.sort()
    triplets=[]
    for i in range(len(arr)-2):
        l=i+1
        r=len(arr)-1
        
        while l<r:

            curSum=arr[i]+arr[l]+arr[r]

            if curSum==target:
                triplets.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
            elif curSum<target:
                l+=1
            elif curSum>target:
                r-=1
    return triplets

array1=[12,3,1,2,-6,5,-8,6]
sum1=0
print(ThreeNumSum(array1,sum1))

