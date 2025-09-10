class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        
        
class BinaryTree():
    def __init__(self):
        self.root=None
        
    def add(self,data):
        c_node=Node(data)
        p=self.root
        
        if self.root==None:
            self.root=c_node
            print(self.root.data)
            
        else:
            while(p is not None):
                if p.data>=data:
                    l=p
                    p=p.left
                    if p is None:
                        l.left=c_node
                        print(f"{l.left.data} this is left")
                    
                else:
                    l=p
                    p=p.right
                    if p is None:
                        l.right=c_node
                        print(f"{l.right.data} this is right")
            p=c_node
            
    def pre_order_traversal(self,root):
        if root is None:
            return 
        print(root.data ,end="-->")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)
        
        
    def in_order_traversal(self,root):
        if root is None:
            return 
        
        self.in_order_traversal(root.left)
        print(root.data ,end="-->")
        self.in_order_traversal(root.right)
        
        
    def post_order_traversal(self,root):
        if root is None:
            return 
        
        self.post_order_traversal(root.left)
       
        self.post_order_traversal(root.right)
        print(root.data ,end="-->")
            
k=BinaryTree()
k.add(4)
k.add(3)
k.add(6)
k.add(1)
k.add(2)
k.add(9)
k.add(10)

k.pre_order_traversal(k.root)
print(" ")

k.in_order_traversal(k.root)

print(" ")
k.post_order_traversal(k.root)

            
            