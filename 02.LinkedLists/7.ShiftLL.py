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

    # print LL
    def PrintLL(self):
        t=self.head
        while t:
            print(t.data)
            t=t.next

    def shiftLL(self,k):
        count=1
        curr=self.head
        
        while curr.next is not None:                
            curr=curr.next
            count+=1
        
        #calculating if k is +ve or -ve
        offset=abs(k) % count
        #if k=0
        if offset ==0:
            return self.head

        #calculate the pos to change links
        pos= count - offset if k>0 else offset
        newTail=self.head

        for i in range(1,pos):
            newTail=newTail.next

        newHead=newTail.next
        newTail.next=None
        curr.next=self.head
        self.head=newHead

        return newHead 


if __name__=='__main__':
    ll=LinkedList()
    ll.Push(5)
    ll.Push(4)
    ll.Push(3)
    ll.Push(2)
    ll.Push(1)
    ll.Push(0)
    print("*"*10)
    ll.PrintLL()
    print("*"*10)
    print("after rotation ")
    ll.shiftLL(2)
    ll.PrintLL()



    
