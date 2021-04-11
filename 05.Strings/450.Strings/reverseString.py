# https://leetcode.com/problems/reverse-string/

def reverseString(arr):
    n=len(arr)
    l=0
    r=len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1

    return arr

a1=['h','e','l','l','o']
print(reverseString(a1))