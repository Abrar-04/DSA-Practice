# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

def Kadane(arr):
    n=len(arr)
    maxSum=arr[0]
    curSum=maxSum

    for i in range(n):
        curSum=max((arr[i]+curSum),arr[i])
        maxSum=max(curSum,maxSum)

    return maxSum



arr=[-2,2,5,-11,6]
print(Kadane(arr))
