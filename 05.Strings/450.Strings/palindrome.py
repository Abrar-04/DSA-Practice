# https://practice.geeksforgeeks.org/problems/palindrome-string0817/1

def palindrome(str):
    l = 0
    r = len(str)-1

    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1

    return True


s1 = 'abcba'
print(palindrome(s1))
