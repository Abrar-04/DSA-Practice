# https://www.geeksforgeeks.org/find-a-specific-pair-in-matrix/


def SpecificPair(arr):
    MAX=0
    n=len(arr)

    for a in range(n-1):
        for b in range(n-1):
            for c in range(a+1,n):
                for d in range (b+1,n):

                    if MAX< (arr[c][d]-arr[a][b]):
                        MAX=arr[c][d]-arr[a][b]
    return MAX

mat = [[ 1, 2, -1, -4, -20 ], 
       [ -8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ], 
       [ -4, -1, 1, 7, -6 ], 
       [ 0, -4, 10, -5, 1 ]]; 
         
print(SpecificPair((mat))) 