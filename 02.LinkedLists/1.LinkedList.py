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

    # insert after a given node
    def InsertAfter(self,prev_node,key):
        if prev_node is None:
            return

        new_node=Node(key)
        new_node.next=prev_node.next
        prev_node.next=new_node

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


    # delete Node
    def DeleteNode(self,pos):
        if self.head is None:
            return

        t=self.head

        if pos==0:
            self.head=t.next
            t=None
            return

        for i in range(pos-1):
            t=t.next
            if t is None:
                break
        if t is None:
            return
        if t.next is None:
            return

        next=t.next.next
        t.next=None
        t.next=next
        

    # print LL
    def PrintLL(self):
        t=self.head
        while t:
            print(t.data)
            t=t.next

    # count
    def Count(self):
        t=self.head
        count=0
        while t:
            count+=1
            t=t.next
        return count

    # search
    def Search(self,key):
        t=self.head
        while t:
            if t.data==key:
                return True
            t=t.next
        return False     


if __name__=='__main__': 
  

    ll = LinkedList() 
    ll.Append(6) 
    ll.Push(7); 
    ll.Push(1); 
    ll.Append(4) 
    ll.InsertAfter(ll.head.next, 8)  

    print ('Created linked list is:' )  
    ll.PrintLL() 

    print("COunt: ",ll.Count())

    print("6 found:",ll.Search(6))

    ll.DeleteNode(2)
    print("del node 2")
    print("Count: ",ll.Count())

    print (' linked list is:' )
    ll.PrintLL() 

    print("8 found: ",ll.Search(8))


        


    
    