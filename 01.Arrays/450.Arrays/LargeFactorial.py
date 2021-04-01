# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1
import sys

def Factorial(x):
    f=1
    if x==0:
        f=1
    elif x==1:
        f=1
    else:
        for i in range(1,x+1):
            f=f*i
    return f

x=14
print(Factorial(x))


def LargeFactorial(n):
    res=[None]*500

    res[0]=1
    res_size=1

    x=2
    while x<=n:
        res_size=multiply(x,res,res_size)
        x+=1
    print("Factorial is ")
    for i in range(res_size,0,-1):
        print(res[i]) 

def multiply(x,res,res_size):

    carry=0
    i=0

    while i<res_size:
        prod=res[i]*x + carry
        res[i]=prod%10 # units digit
        carry=prod//10 # tens digit
        i+=1
    
    while(carry):
        res[res_size]=carry%10 
        carry=carry//10
        res_size+=1

    return res_size

f=100
print(LargeFactorial(f))


    