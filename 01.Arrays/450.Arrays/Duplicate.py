# https://leetcode.com/problems/find-the-duplicate-number/

def Duplicate(arr):
    
    arr.sort()
    n=len(arr)
    i=0
    for i in range(n):
        if arr[i]==arr[i+1]:
            return arr[i]


arr=[1,3,4,2,2]
print(Duplicate(arr))



# Floyd cycle
def twoPointerApproach(arr):
    fast=arr[0]
    slow=arr[0]

    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]

        if fast==slow:
            break

    slow=arr[0]

    while fast != slow :
        slow=arr[slow]
        fast=arr[fast]

    return fast

arr=[1,3,4,2,7,8,6,2]
print(twoPointerApproach(arr))


