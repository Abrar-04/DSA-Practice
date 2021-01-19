# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1

def MinimiseMaxHts(arr,k):

    x=min(arr)    
    y=max(arr)   
    y=y-k
    x=x+k
    diff=y-x

    return diff

arr=[3,9,12,16,20]
k=3
print(MinimiseMaxHts(arr,k))