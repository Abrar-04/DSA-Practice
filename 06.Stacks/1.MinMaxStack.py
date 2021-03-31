class MinMaxStack:
    def __init__(self):
        self.minMaxStack=[]
        self.Stack=[]

    def peek(self):
        return self.Stack[len(self.Stack)-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.Stack.pop()

    def push(self,num):
        newMinMax={'min':num,'max':num}
        if len(self.minMaxStack):
            lastMinMax=self.minMaxStack[len(self.minMaxStack)-1]
            newMinMax['min']=min(lastMinMax['min'],num)
            newMinMax['max']=max(lastMinMax['max'],num)
        self.minMaxStack.append(newMinMax)
        self.Stack.append(num)

    def getMin(self):
        print("MIN: ",self.minMaxStack[len(self.minMaxStack)-1]['min'])
        return self.minMaxStack[len(self.minMaxStack)-1]['min']

    def getMax(self):
        print("MAX: ",self.minMaxStack[len(self.minMaxStack)-1]['max'])
        return self.minMaxStack[len(self.minMaxStack)-1]['max']

    def print(self):
        print(self.Stack)

if __name__=='__main__': 
    mms=MinMaxStack()
    mms.push(30)
    mms.push(50)
    mms.push(10)
    mms.getMax()
    mms.getMin()
    mms.print()
    print("after pop")
    mms.pop()
    mms.getMax()
    mms.getMin()
    mms.print()