class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None

    # insert at front
    def Push(self,key):
        new_node=Node(key)
        new_node.next=self.head

        if self.head is not None:
            self.head.prev=new_node
        
        self.head=new_node


    # insert after a pos
    def InsertAfter(self,pos,key):
        if pos is None:
            return
            
        new_node=Node(key)
        new_node.next=pos.next
        pos.next=new_node
        new_node.prev=pos

        if new_node.next is not None:
            new_node.next.prev=new_node

    
    # insert at end
    def Append(self,key):
        
        new_node=Node(key)
        new_node.next=None

        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        
        last=self.head

        while last.next is not None:
            last=last.next

        last.next=new_node
        new_node.prev=last


    # delete node
    def DeleteNode(self,pos):
        if self.head is None or pos is None:
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
        t.prev=pos



    # print
    def PrintDLL(self):
        t=self.head
        while t is not None:
            print(t.data)
            last=t
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
    dll = DoubleLinkedList()
    dll.Append(6) 
    dll.Push(7) 
    dll.Push(1) 
    dll.Append(4) 

    
    dll.PrintDLL() 
    print("*"*10)
    print("Count: ",dll.Count())
    print("*"*10)
    print("6 found: ",dll.Search(6))
    print("*"*10)
    dll.DeleteNode(2)
    print("*"*10)
    print("del node 2")
    print("*"*10)
    print (' linked list is:' )
    dll.PrintDLL() 
    print("*"*10)
    print("Count: ",dll.Count())
    print("*"*10)
    print("6 found: ",dll.Search(6))
    print("*"*10)
