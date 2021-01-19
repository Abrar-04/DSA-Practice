# https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1

def KthEle(arr,k):
    arr.sort()

    return arr[k-1]

a=[3,4,8,1,9,5]
print(KthEle(a,3))
