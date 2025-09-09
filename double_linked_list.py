class Node():
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
        
class Double_linked_list():
    def __init__(self):
        self.head=None
        self.tail=None
        
        
    def add(self,data):
        c_node=Node(data)
        if self.head is None:
            self.head=c_node
            self.tail=c_node
        else:
            p=self.head
            while(p.next is not None):
                p=p.next
            p.next=c_node
            c_node.prev=p
            self.tail=c_node
            
            
    def print(self):
        p=self.tail
        while(p):
            print(p.data,end="--->")
            p=p.prev
        print("None")
        
k=Double_linked_list()
k.add(4)
k.add(3)
k.add(2)
k.print()