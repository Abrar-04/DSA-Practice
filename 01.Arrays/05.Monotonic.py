def Monotonic(arr):
    inc=True
    dec=True

    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            dec=False
        elif arr[i]<arr[i-1]:
            inc=False
    
    return inc or dec


array1=[-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
print(Monotonic(array1))