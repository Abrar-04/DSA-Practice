class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    

    # insert at the end
    def Append(self,key):
        new_node=Node(key)

        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while (last.next):
            last=last.next

        last.next=new_node


    #print
    def PrintLL(self):
        t=self.head
        while t:
            print(t.data)
            t=t.next

def MergeLL(h1,h2):
    p1=h1
    tail=None
    p2=h2

    while p1 is not None and p2 is not None:
        if p1.data<p2.data:
            tail=p1
            p1=p1.next
        else:
            if tail is not None:
                tail.next=p2
            tail=p2
            p2=p2.next
            tail.next=p1

    if p1 is None:
        tail.next=p2

    return h1 if h1.data<h2.data else h2



if __name__=='__main__': 
    LL1=LinkedList()
    LL1.Append(2)
    LL1.Append(6)
    LL1.Append(7)
    LL1.Append(8)
    print("*"*10)
    LL1.PrintLL()
    print("*"*10)
    LL2=LinkedList()
    LL2.Append(1)
    LL2.Append(3)
    LL2.Append(4)
    LL2.Append(5)
    LL2.Append(9)
    LL2.Append(10)
    LL2.PrintLL()
    print("*"*10)
    a=LL1.head
    b=LL2.head
    LL1.head=MergeLL(a,b)
    LL1.PrintLL()
    print("*"*10)
