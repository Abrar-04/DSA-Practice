'''
logic seems correct , 
but there is an error with elements less than k, 
idk wts wrong, im stuck

'''








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

def RearrangeLL(head,k):
    smallHead=None
    smallTail=None
    equalHead=None
    equalTail=None
    greatHead=None
    greatTail=None


    node=head

    while node is not None:

        if node.data < k:
            #small
            smallHead,smallTail=growLL(smallHead,smallTail,node)
                
        elif node.data>k:
            #great
            greatHead,greatTail=growLL(greatHead,greatTail,node) 

        else:
            #equal
            equalHead,equalTail=growLL(equalHead,equalTail,node)

            #override the .next of curr node
        prev=node
        node=node.next
        prev.next=None

    firstHead,firstTail=connectLL(smallHead,smallTail,equalHead,equalTail)
    finalHead,finalTail=connectLL(firstHead,firstTail,greatHead,greatTail)

    return finalHead


def growLL(head,tail,node):

    newHead=head
    newTail=node

    if newHead is None:
        newHead=node
        
    if tail is not None:
        tail.next=node

    return (newHead,newTail)


def connectLL(h1,t1,h2,t2):

    newHead= h2 if h1 is None else h1 
    newTail= t1 if t2 is None else t2

    if t1 is not None:
        t1.next=h2

    return (newHead,newTail)

def PrintLL(head):
    t=head
    while t:
        print(t.data)
        t=t.next


if __name__=='__main__':
    ll=LinkedList()
    ll.Push(4)
    ll.Push(1)
    ll.Push(2)
    ll.Push(5)
    ll.Push(0)
    ll.Push(3)
    print("*"*10)
    ll.PrintLL()
    print("*"*10)
    print("after rearrange ")
    RearrangeLL(ll.head,3)
    PrintLL(RearrangeLL(ll.head,3))
        
            

        


          


