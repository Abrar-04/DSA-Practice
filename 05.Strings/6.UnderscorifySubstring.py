def driver(string,sub):
    locations = collapse(getLocations(string,sub))

    return underscorify(string,locations)

# getLocations() gets the indices of the sub in string and saves in locations[[]]
def getLocations(string,sub):
    locations=[]
    startIdx=0

    while startIdx<len(string):
        nextIdx=string.find(sub,startIdx)
        
        if nextIdx!=-1:
            locations.append([nextIdx,nextIdx+len(sub)])
            startIdx=nextIdx+1
        else:
            break

    return locations

# collapse() makes sure that there are no two adjacent undescores(_) and
# lets [[a,b],[c,d]] 
#  if b>c : 
# then [[a,d]]
#  store them in newLocations 
def collapse(locations):

    if not len(locations):
        return locations

    newLocations=[locations[0]]
    prev=newLocations[0]

    for i in range(1,len(locations)):
        curr=locations[i]

        if curr[0]<=prev[1]:
            prev[1]=curr[1]
        else:
            newLocations.append(curr)
            prev=curr

    return newLocations


# this adds an underscore at the indices found from newLocations 
# it dynamically modifies the index [a,b] when needed and compares 
# if it is inBetweenUnderscores it moves ahead and adds the string accordingly and adds a '_' when ends
# and proceeds forward
def underscorify(string,locations):
    locationIdx=0
    stringIdx=0
    inBetweenUnderscores=False
    finalChars=[]
    i=0

    while stringIdx<len(string) and locationIdx<len(locations):
        if stringIdx==locations[locationIdx][i]:
            finalChars.append("_")
            inBetweenUnderscores=not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationIdx+=1
            i=0 if i==1 else 1

        finalChars.append(string[stringIdx])
        stringIdx+=1
    
    if locationIdx<len(locations):
        finalChars.append("_")
    elif stringIdx<len(string):
        finalChars.append(string[stringIdx:])


    return "".join(finalChars)



sentence="testthis is a testtest to see if testestest it works"
word="test"
print("Before \n",sentence)
print("\n After \n")
print(driver(sentence,word))
