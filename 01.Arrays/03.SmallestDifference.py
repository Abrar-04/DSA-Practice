def SmallestDifference(a1,a2):

    a1.sort()
    a2.sort()
    i=0
    j=0
    small=float('inf')
    curr=float('inf')
    smallPair=[]
    
    while i<len(a1) and j<len(a2):
        first=a1[i]
        second=a2[j]

        if first< second:
            curr=second-first
            i+=1
        elif second<first:
            curr=first-second
            j+=1
        else :
            return [first,second]
        
        if small>curr:
            small=curr
            smallPair=[first,second]

    return smallPair



array1=[-1,5,10,20,28,3]
array2=[26,134,135,15,17]
print(SmallestDifference(array1,array2))