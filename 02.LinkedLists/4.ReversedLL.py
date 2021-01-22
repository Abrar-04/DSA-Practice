class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    # insert at beginning
    def Push(self,key):
        new_node=Node(key)
        new_node.next=self.head
        self.head=new_node

    def ReversedLL(self):
        p1=None
        p2=self.head

        while p2:
            p3=p2.next
            p2.next=p1
            p1=p2
            p2=p3
        self.head=p1

    # print LL
    def PrintLL(self):
        t=self.head
        while t:
            print(t.data)
            t=t.next

if __name__=='__main__': 
    ll=LinkedList()
    ll.Push(5)
    ll.Push(4)
    ll.Push(3)
    ll.Push(2)
    ll.Push(1)
    ll.Push(0)
    ll.PrintLL()
    print("*"*10)
    print("reversed")
    ll.ReversedLL()
    ll.PrintLL()