##########################
    # HASH TABLE #
def groupAnagrams(words):
    anagrams={}
    
    for w in words:
        sortwords="".join(sorted(w))

        if sortwords in anagrams:
            anagrams[sortwords].append(w)
        else:
            anagrams[sortwords]=[w]

    a=list(anagrams.values())

    return a

x=['oy','yo','act','cat','tac','flop','olfp']
print(groupAnagrams(x))



###########################################################################3
    # array of indices , array of sorted words,  map them and make lists #

def GROUPanagrams(words):

    if len(words)==0:
        return []

    sortwords=["".join(sorted(w)) for w in words]
    indices=[i for i in range(len(words))]
    indices.sort(key=lambda x:sortwords[x])

    result=[]
    curAnagramGrp=[]
    curAnagram=sortwords[indices[0]]

    for i in indices:
        w=words[i]
        sword=sortwords[i]

        if sword == curAnagram:
            curAnagramGrp.append(w)
            continue

        result.append(curAnagramGrp)
        curAnagramGrp=[w]
        curAnagram=sword
        
    result.append(curAnagramGrp)

    return result

x=['oy','yo','act','cat','tac','flop','olfp']
print(GROUPanagrams(x))
