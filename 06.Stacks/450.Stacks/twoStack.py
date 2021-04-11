class twoStack():
    def __init__(self,n):
        self.size=n
        self.arr=[None]*self.size
        self.top2=self.size//2
        self.top1=(self.size//2) +1
    
    def push1(self,x):
        if(self.top1>0):
            self.top1-=1
            self.arr[self.top1]=x
        else:
            print("Stack 1 overflown")

    def push2(self,x):
        if (self.top2<self.size-1):
            self.top2+=1
            self.arr[self.top2]=x

        else:
            print("Stack 2 overflown")


    def pop1(self):
        if (self.top1<=self.size//2):
            x=self.arr[self.top1]
            self.top1+=1
            return x
        else:
            print("Stack Undeflow")

    def pop2(self):
        if(self.top2>=(self.size//2) +1):
            x=self.arr[top2]
            self.top2-=1
            return x

        else:
            print("Stack Undeflow")

    def printStack(self):
        print(self.arr)
    
if __name__=='__main__':
    ts=twoStack(5)
    ts.push1(5)
    ts.push1(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    ts.printStack()



    
