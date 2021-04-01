#https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/


'''
we take sum of every element in arr
if same sum is repeated then their difference is zero
so sum of subArr is zero

eg:
4,2,-3,1,6
(4,4+2,4+2-3,4+2-3+1,4+2-3+1+6)
sum: 4,6,3,4,10
4,4found 

'''
def SubArrSum0(arr):
    n=len(arr)

    s=[None]*n
    SubSum=0

    for i in range(n):
        SubSum+=arr[i]

        if SubSum==0 or SubSum in s:
            return True
        s.append(SubSum)
            
        
    return False

arr=[4,2,-3,1,6]
print(SubArrSum0(arr))