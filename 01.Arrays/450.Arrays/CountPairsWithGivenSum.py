# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

def CountPairsWithGivenSum(arr,sum):
    n=len(arr)
    c=0

    for i in range(n):
        for j in range(i+i,n):
            if arr[i]+arr[j]==sum:
                c+=1
    return c

arr=[1,5,7,5]
sum=6
print(CountPairsWithGivenSum(arr,sum))        

# optimized
# use of maps

def optimized(arr,sum):
    n=len(arr)

    m=[0]*1000 

    for i in range(n):
        m[arr[i]]+=1 # count of elements in respective index

    doubleCount=0 
    
    # subtract the sum with every element 
    # and check if a pair is found 
    # and if it exists in the hash then 
    # add it 
    # and finally divide by 2 
    # as every pair is iterated twice
    for i in range(n):
        doubleCount+=m[sum-arr[i]]

        if (sum-arr[i]==arr[i]): # arr[i],arr[i] not valid
            doubleCount-=1

    return doubleCount//2


print("optimized")
arr1=[1,5,7,5]
sum1=6
print(optimized(arr1,sum1))   
