'''
ord(letter) gives unicode of the letter
a:97
z:122
'''


def CaesarCipherEncryptor(string,key):
    newL=[]
    newKey=key%26

    for l in string:
        newL.append(getLetter(l,newKey))

    return "".join(newL)

def getLetter(letter,key):
    newL=ord(letter)+key

    if newL<=122:
        return chr(newL)
    else:
        return chr(96+newL%122)

s='xyz'
k=2
print(CaesarCipherEncryptor(s,k))




############################################################

'''
create a string list of alphabets n make use indices 
'''

def cce(string,key):
    newLetters=[]
    newKey=key%26
    alphabet=list("abcdefghijklmnopqrstuvwxyz")

    for l in string:
        newLetters.append(getLetterAlphabet(l,newKey,alphabet))

    return "".join(newLetters)

def getLetterAlphabet(letter,key,alphabet):
    newCode=alphabet.index(letter)+key

    if newCode<=25:
        return alphabet[newCode]
    else:
        return alphabet[-1 + newCode%25]


s='xyz'
k=2
print(cce(s,k))
