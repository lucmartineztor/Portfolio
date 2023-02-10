
class Node :   
    def __init__(self,data,next =None):
        self.data = data
        self.next = next



class Linkedlist:   
    def __init__(self,head):
        self.head = head   
    
    def print_parse_list(self):
        curr = self.head
        while (curr != None):
            print (curr.data)
            curr = curr.next

    def insert(self,data,number=1):
        if number>0:
            try:
                curr = self.head
                newNode = Node(data)
                p=0
                while p<number:
                    curr = curr.next
                    p=p+1
                Curr=curr.next
                curr.next=newNode
                newNode.next = Curr
            except:
                print('element out of range')
        else:
            try:
                newNode=Node(0)
                newNode.next=node1
                global mylinkedlist
                mylinkedlist =  Linkedlist(newNode)
        
            except:
                newNode=Node(0)
        


    def count(self):
        curr = self.head
        add=0
        while (curr != None):
            add = add+curr.data
            curr = curr.next
        return add



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4



mylinkedlist =  Linkedlist(node1)

print('Write an insert function for Linked list')

mylinkedlist.insert(0,0)
mylinkedlist.insert(4,3)
mylinkedlist.print_parse_list()



print('Linked list sumWrite a function, linkedlist_sum, that takes in the head of a linked list that contains number values.The function should return the total sum of all values in the linked.')

print(mylinkedlist.count())


'''


BINARY TREES


'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



    def Tree_includes (self,number):
        if self.data == number:
            return True
        else:
            return False

    def Insert(self, data, direction ):
        
        if self.data:
            if direction=='left':
                if self.left is None:
                   self.left = Node(data)
                else:
                   self.left.Insert(data,'left')
            if direction=='right':
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Insert(data,'right')
        else:
            self.data = data

                


    def tree_min_value(self):
        
        if self.left:
            
            self.left.tree_min_value()
            
        if self.right:
            
            
            self.right.tree_min_value()
        
        
        
        TotalValues.append( self.data)   
               
    def bottom_right_value(self):
        
        if self.right:

            self.right.bottom_right_value()
        
        TotalValuesRight.append(self.data)


    def root_path(self, data): 
        if self.data== data:
            return 0
        for node in (self.left, self.right):
            if node != None:                              
                count = node.root_path(data)
                if count != None:
                    return count + 1
        return None

       

TotalValues=[]
TotalValuesRight=[]
root=Node(27)

print('tree includes Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.')

tree_includes=root.Tree_includes(28)
print(tree_includes)
tree_includes= root.Tree_includes(27)
print(tree_includes)


root.Insert(4,'right')


root.Insert(20,'right')


root.Insert(23,'left')


print('tree min value Write a function, tree_min_value, that takes in the root of a binary tree that contains number values.The function should return the minimum value within the tree.You may assume that the input tree is non-empty. ')




  
root.tree_min_value()
MinValue=TotalValues[0]
for i in range(len(TotalValues)):
    if TotalValues[i]<MinValue:
        MinValue=TotalValues[i]

print(MinValue)
print('bottom right value Write a function, bottom_right_value, that takes in the root of a binary tree.The function should return the right-most value in the bottom-most level of the tree.You may assume that the input tree is non-empty.')



root.bottom_right_value()
print(TotalValuesRight[0])

print('Shortest path Write a function that takes in the root of a binary tree and a value and return the shortest path between the root and that value (you may assume there is one of this value in the tree')


print(root.root_path(20))










 