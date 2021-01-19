def LargestRange(arr):
    best=[]
    longlen=0
    nums={}

    for num in arr:
        nums[num]=True
    for num in arr:
        if not nums[num]:
            continue
        nums[num]=False
        curlen=1
        lhs=num-1
        rhs=num+1

        while lhs in nums:
            nums[lhs]=False
            lhs-=1
        while rhs in nums:
            nums[rhs]=False
            rhs+=1
        if curlen>longlen:
            longlen=curlen
            best=[lhs+1,rhs-1]

    return best


array1=[1,11,3,0,15,5,2,4,10,7,12,6]
print(LargestRange(array1))