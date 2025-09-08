class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class Linked_list():
    def __init__(self):
        self.head=None
        
    def add(self,data):
        c_node=Node(data)
        if self.head is None:
            self.head=c_node
        else:
            p=self.head
            while(p.next is not None):
                p=p.next
            p.next=c_node
    def print(self):
        p=self.head
        while(p):
            print(p.data,end="--->")
            p=p.next
        print("None")
            
            
         
         
k=Linked_list()
k.add(4)
k.add(3)
k.add(2)
k.print()