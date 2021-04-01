# https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1


'''
similar to KADANE
'''
def MaxSubArrProduct(arr):
    n=len(arr)

    localMin=localMax=globalMax=arr[0]

    for i in range(1,n):
        temp=localMin # store curr local Min

        # select max of ( current element, current element*local max, current element*local max )
        localMax=max(arr[i],arr[i]*localMax,arr[i]*localMin) 
        # select min of ( current element, current element*local min, current element* initial local min )
        localMin=min(arr[i],arr[i]*localMin,arr[i]*temp)
        #select max product 
        globalMax=max(globalMax,localMax)


    return globalMax

arr=[6,-3,-10,-5,0,2] # 180 (6,-3,-10)

print(MaxSubArrProduct(arr))