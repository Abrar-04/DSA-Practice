def isPalindrome(string):
    reversedString=""
    for i in reversed(range(len(string))):
        reversedString+=string[i]

    return string==reversedString

#######################################################

def isPalindromeBest(string):
    left=0
    right=len(string)-1

    while left<right:
        if string[left] != string[right]:
            return False

        left+=1
        right-=1

    return True


s='abcdcba'
print(isPalindrome(s))
print(isPalindromeBest(s))