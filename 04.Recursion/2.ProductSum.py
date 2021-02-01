def ProductSum(arr,depth=1):
    Sum=0

    for ele in arr:
        if type(ele) is list:
            Sum+=ProductSum(ele,depth+1)
        else:
            Sum+=ele

    return Sum*depth

ARR=[5,2,[7,-1],3,[6,[-13,8],4]]
print(ProductSum(ARR))
