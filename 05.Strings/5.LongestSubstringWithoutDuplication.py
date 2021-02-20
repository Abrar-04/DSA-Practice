def longestSubstringWithoutDuplication(string):
    lastSeen={}
    longest=[0,1]
    start=0

    for i,ch in enumerate(string):
        if ch in lastSeen:
            start=max(start,lastSeen[ch]+1)
        
        # start:beginning of non duplicated substr , i:where duplication occurs  to take diff we add 1 
        # update the longest length n=w/o duplicaiton
        if longest[1]-longest[0] < i+1-start:
            longest=[start,i+1]
        
        # update the duplicated with new position
        lastSeen[ch]=i
    
    return string[longest[0]:longest[1]]


x='clementisacap'
print(longestSubstringWithoutDuplication(x))

