# https://leetcode.com/problems/search-a-2d-matrix/


def SearchMatrix2loops(arr,target):

    for i in range(len(arr)):
        if target<=arr[i][len(arr)-1]:
            for j in range(len(arr[i])):
                if arr[i][j]==target:
                    return True
    return False

def SearchMatrix(arr,target):
    def BinarySearh(arr,target):
        mid=0
        low=0
        high=len(arr)
        c=0

        while low<=high:
            c+=1
            mid=(low+high)//2

            if target==arr[mid]:
                return True

            elif target<arr[target]:
                high=mid-1
            
            elif target>arr[target]:
                low=mid+1

        return False

    for x in range(len(arr)):
        if arr[x][-1]>=target:
            return BinarySearh(arr[x],target)
    return False


array=[ [1 ,2 ,3 ,4],
        [5 ,6 ,7 ,8],
        [9,10,11 ,12],
        [13,14,15,16]]

print(SearchMatrix2loops(array,7))
print(SearchMatrix(array,7))
