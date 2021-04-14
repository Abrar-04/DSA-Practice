# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

def minJumps(arr):
    n=len(arr)
    reachablePos=0

    for i in range(n):
        if reachablePos<i:
            return False
        reachablePos=max(reachablePos,i+arr[i])

    return True


a1=[1,1,2,5,2,1,0,0,1,3]
print(a1)
print(minJumps(a1))

a2=[1,1,2,3,2,1,0,0,1,3]
print(a2)
print(minJumps(a2))
