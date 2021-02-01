# https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

def rotate90(a):
    n=len(a)

    for i in range(n//2):
        for j in range(i,n-i-1):
            t=a[i][j]
            a[i][j]=a[n-1-j][i]
            a[n-1-j][i]=a[n-1-j][i]
            a[n-1-j][i]=a[n-1-i][n-1-j]
            a[n-1-i][n-1-j]=a[j][n-1-i]
            a[j][n-1-i]=t
            
    n=len(a)
    for i in range(n):
        print(a[i])


array=[[1,2,3],
     [4,5,6],
     [7,8,9]]
     

print(rotate90(array))
