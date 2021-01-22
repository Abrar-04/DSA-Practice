class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    # find loop
    def FindLoop(self):
        t=self.head
        f=t.next
        s=t.next.next

        while f!=s:
            f=f.next
            s=s.next.next
        f=t
        
        while f!=s:
            f=f.next
            s=s.next

        return f
