class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    #insert at beginning
    def Push(self,key):
        new_node=Node(key)
        new_node.next=self.head
        self.head=new_node

    # count
    '''
    def Count(self):
        t=self.head
        c=0
        while t:
            c=+1
            t=t.next
        return c
    '''
    
    # print
    def PrintLL(self):
        t=self.head
        while t:
            print(t.data)
            t=t.next
    

    # remove from end
    def RemoveFromEndandPrint(self,x):
        t=self.head
        f=self.head
        s=self.head
        c=1

        while c<=x:
            s=s.next
            c+=1
            
        if s is None:
            t.data=t.next.data
            t.next=t.next.next
            return
        
        while s.next is not None:
            s=s.next
            f=f.next

        f.next=f.next.next

        t=self.head
        while t:
            print(t.data)
            t=t.next
        

if __name__=='__main__':     
    ll=LinkedList()
    ll.Push(9)
    ll.Push(8)
    ll.Push(7)
    ll.Push(6)
    ll.Push(5)
    ll.Push(4)
    ll.Push(3)
    ll.Push(2)
    ll.Push(1)
    ll.Push(0)
    print("Before Deletion")
    ll.PrintLL()
    print("*"*10)
    ll.RemoveFromEndandPrint(4)

