def Nfibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else :
        return Nfibonacci(n-1)+Nfibonacci(n-2)

##########################################################

def HashFib(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n]=HashFib(n-1,memoize)+HashFib(n-1,memoize)

        return memoize[n]

print(HashFib(8))
