class Nstacks:

    def __init__(self,k,n):
        self.k=k # #of stacks
        self.n=n # size of all stacks

        self.arr=[0]*self.n #initialise and arr with k stacks

        self.top=[-1]*self.k # all k stacks are empty

        self.free=0 # top of free stack\

        self.next= [i+1 for i in range(self.n)] # point to next ele
        self.next[self.n -1]=-1 # point till last ele
    
    def isEmpty(self,sn):
        return self.top[sn]==-1

    def isFull(self):
        return self.free ==-1

    def push(self,item,sn):
        if self.isFull():
            print("STACK OVERFLOWN")
            return
        
        insert_at=self.free #insert at the first free pos

        self.free=self.next[self.free] # move free pos
        self.arr[insert_at]=item #insert the item in free pos
        self.next[insert_at]=self.top[sn] # move top pos
        self.top[sn]=insert_at #new top

    def pop(self,sn):
        if self.isEmpty(sn):
            print("STACK UNDERFLOWN")
            return None
        
        topOfStack=self.top[sn] # item at top of stack
        self.top[sn]=self.next[self.top[sn]] # new top
        self.next[topOfStack] #old top is moved to free pos
        self.free=topOfStack

        return self.arr[topOfStack]

    def printStack(self,sn):
        topIndex=self.top[sn]
        while topIndex!=-1:
            print(self.arr[topIndex])
            topIndex=self.next[topIndex]

    def printAll(self):
        
        for i in range(self.n):
            print(self.arr[i])


if __name__=='__main__':

    NS=Nstacks(4,16)

    NS.push(1000,0)
    NS.push(800,0)
    NS.push(900,0)
    NS.push(700,0)

    NS.push(121,1)
    NS.push(189,1)
    NS.push(165,1)
    NS.push(132,1)

    NS.push(265,2)
    NS.push(244,2)
    NS.push(211,2)
    NS.push(278,2)

    NS.push(369,3)
    NS.push(344,3)
    NS.push(311,3)
    NS.push(355,3)


    print("*"*10)    
    print("*"*10)
    NS.printAll()
    print("*"*10)
    print("*"*10)

    print("")
    print("")

    print("*"*10)
    NS.printStack(0)
    print("*"*10)
    NS.printStack(1)
    print("*"*10)
    NS.printStack(2)
    print("*"*10)
    NS.printStack(3)
    print("*"*10)


    print("popped from 0 ",NS.pop(0))
    print("popped from 1 ",NS.pop(1))
    print("popped from 2 ",NS.pop(2))
    print("popped from 3 ",NS.pop(3))


    print("*"*10)
    NS.printAll()
