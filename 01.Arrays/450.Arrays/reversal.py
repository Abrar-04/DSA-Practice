#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

def reverseArr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

array1=[1,2,3,4,5,6]
print("Original: ",array1)
print("Reversed: ",reverseArr(array1,0,5))
