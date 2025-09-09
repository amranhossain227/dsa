class stack():
    def __init__(self):
        self.stack=[]
        
    def push(self,data):
        self.stack.append(data)
        
        
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if (self.is_empty()):
            return "stack is empty"
        else:
            return self.stack.pop()
        
l=stack()
l.push(4)
l.push(3)
l.push(2)
print(l.stack)
l.pop()
print(l.stack)



# do it with linked list

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack_linked_list():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def push(self,data):
        c_node=Node(data)
        if self.head is None:
            self.head=c_node
            self.tail=c_node
        else:
            self.tail.next=c_node
            self.tail=c_node
    def is_empty(self):
        return self.head is None
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            p=self.head
            if p.next is None:
                self.head=None
                self.tail=None
                return p.data
            while(p.next.next is not None):
                p=p.next
            r=p.next
            p.next=None
            self.tail=p
            return r.data
        
        
    def print(self):
        p=self.head
        while(p):
            print(p.data,end="--->")
            p=p.next
        print("None")
        
        
k=Stack_linked_list()
k.push(4)
k.push(3)
k.push(2)
k.print()
k.pop()
k.print()