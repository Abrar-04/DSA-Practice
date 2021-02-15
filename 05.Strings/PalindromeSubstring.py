def longPalSub(string):
    curLong=[0,1]
    for i in range(1,len(string)):
        odd=getLongPal(string,i-1,i+1)
        even=getLongPal(string,i-1,i)
        long=max(odd,even,key=lambda x: x[1]-x[0])
        curLong=max(long,curLong,key=lambda x: x[1]-x[0])

    return string[curLong[0]:curLong[1]]

def getLongPal(string,left,right):
    while left>=0 and right<len(string):
        if string[left]!=string[right]:
            break
        left-=1
        right+=1

    return[left+1,right]

s='abaxyzzyxf'
print(longPalSub(s))