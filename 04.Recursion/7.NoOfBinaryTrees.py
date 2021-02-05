def NoOfBinaryTreesFormula(n):
    return catalan(n)

def catalan(n):
    # 2n.C.n / n+1
    # Formula derived based on observations   
    cat=int ( ( 1/(n+1) ) * ( (factorial(2*n)) // (factorial(n))**2 ) )
    return cat

def factorial(x):
    if x==0 or x==1:
        return x 
    else:
        return x * factorial(x-1)

###################################################################################3333

def RecursiveBinaryTrees(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    
    totalTrees=0

    for leftTreeNodes in range(0,n):
        rightTreeNodes = n-1-leftTreeNodes
        leftTrees=RecursiveBinaryTrees(leftTreeNodes)
        rightTrees=RecursiveBinaryTrees(rightTreeNodes)
        totalTrees+=leftTrees*rightTrees

    return totalTrees



nodes=4
print("Catalan: ",NoOfBinaryTreesFormula(nodes))
print("Recursive: ",RecursiveBinaryTrees(nodes))





