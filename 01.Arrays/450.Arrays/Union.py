#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

def Union(arr1,arr2,arr3):
    arr4=[]
    
    arr4=arr1+arr2+arr3
    arr4=list(set(arr4))
    arr4.sort()


    return arr4

arr1=[85,25,32,54,6]
arr2=[85,2]
arr3=[6,2]
print(Union(arr1,arr2,arr3))
