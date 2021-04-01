# https://practice.geeksforgeeks.org/problems/common-elements1132/1


#time 
#space O(n)
def CommonElements(ar1,arr2,arr3):

    i=0 #arr1
    j=0 #arr2
    k=0 #arr3

    common=[]

    n1=len(arr1)
    n2=len(arr2)
    n3=len(arr3)

    while i<n1 and j<n2 and k<n3:

        # compare first and second arr, second and third ,
        # if match found display and mov forward
        # if not match
        # check carrays separareltty
        # as arrays are sorted order , direct incrementing will be enough 
        # if the arr[i]<arr2[j] then increment i
        # if arr2[j]<arr3[k] then incremernt j
        # (if arr3[k]<arr1[i]) then incremern k

        #display the common element here
        if (arr1[i]==arr2[j] and arr2[j]==arr3[k]):
            common.append(arr1[i])
            i+=1
            j+=1
            k+=1

        elif (arr1[i]<arr2[j]):
            i+=1
        
        elif (arr2[j]<arr3[k]):
            j+=1

        elif (arr3[k]<arr1[i]):
            k+=1

    return common

arr1=[1, 5, 10, 20, 40, 80]
arr2=[6, 7, 20, 80, 100]
arr3=[3, 4, 15, 20, 30, 70, 80, 120]

print(CommonElements(arr1,arr2,arr3))


        
        


