# https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

def NegPos(arr):
    i=0
    for j in range(0,len(arr)):
        if arr[j]<0 :
            arr[i],arr[j]=arr[j],arr[i]
            i+=1


    return arr

def twopointer(arr):

    left=0
    right=len(arr)-1

    while left<=right:

        if arr[left] < 0 and arr[right] < 0:
            left+=1

        elif arr[left]>0 and arr[right]<0:
            arr[left], arr[right] = arr[right],arr[left]
            left+=1
            right-=1

        elif arr[left]>0 and arr[right]>0:
            right-=1

        elif arr[left ]<0 and arr[right]>0 :
            left+=1
            right-=1

    return arr


a=[-5,2,3,11,6,-2,-3,-8,7,8]
print(NegPos(a))
print(twopointer(a))
