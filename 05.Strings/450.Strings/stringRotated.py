# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

def stringRotated(str1, str2):
    s1=len(str1)
    s2=len(str2)

    if s1!=s2:
        return False
    
    temp=str1+str1

    if temp.count(str2)>0:
        return True

    else:
        return False

str1='abcd'
str2='cdab'
# abcdabcd
print(stringRotated(str1,str2))



