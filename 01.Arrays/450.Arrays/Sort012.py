# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

def Sort012(arr):
    zeros=0
    ones=0
    twos=0

    for num in arr:
        if num==0:
            zeros+=1
        elif num==1:
            ones+=1
        elif num==2:
            twos+=1
    
    i=0

    while zeros or ones or twos:
        if zeros:
            arr[i]=0
            i+=1
            zeros-=1
            continue
        elif ones:
            arr[i]=1
            i+=1
            ones-=1
            continue
        elif twos:
            arr[i]=2
            i+=1
            twos-=1
            continue

    return arr

a=[0,2,1,2,0]
print(Sort012(a))

