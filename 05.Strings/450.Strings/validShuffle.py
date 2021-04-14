# https://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-of-two-other-given-strings/

def validShuffle(testStr,str1,str2):
    t=len(testStr)
    s1=len(str1)
    s2=len(str2)
    i,j,k=0,0,0
    #i->str1,j->str2,k->testStr,
    if t!=s1+s2:
        return False
    

    # checks if str1,str2 available in testStr
    while k!=t:
        if i<s1 and str1[i]==testStr[k]:
            i+=1
        elif j<s2 and str2[j]==testStr[k]:
            j+=1
        else:
            return False
        k+=1

    return True


a='AB'
b='CD'
c='ACGB'
print(validShuffle(c,a,b))
    
