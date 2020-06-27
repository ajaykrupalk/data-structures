class Node:
  def __init__(self,val):
    self.left=None#stores the left node
    self.right=None#stored the right node
    self.v=val#stores value of node

class Tree:
  def __init__(self):
    self.root=None#initialising the root to None

  def getRoot(self):
    return self.root#gets the root of the tree

  def add(self,val):
    if self.root is None:#if tree is empty
      self.root=Node(val)#root=value
    else:
      self._add(val,self.root)#add to the tree

  def _add(self,val,node):
    if val<node.v:#value is less than the root or parent node
      if node.left is not None:#if the left node is not empty
        self._add(val,node.left)#recursion is performed
      else:#if left node is empty, assign the value
        node.left=Node(val)
    else:
      if node.right is not None:
        self._add(val,node.right)
      else:
        node.right=Node(val)

  def find(self,val):
    if self.root is not None:#if the tree is not empty
      self._find(val,self.root)
  
  def _find(self,val,node):
    if val==node.v:#if given value and node are same
      print(f"\nFound the value:{val}")
    elif val<node.v and node.left is not None:#searching for left sub-tree
      self._find(val,node.left)
    elif val>node.v and node.right is not None:#searching for right sub-tree
      self._find(val,node.right)
    else:
      print("Value not found")
  
  def deleteTree(self):
    self.root=None
    print("Tree is deleted")

  def printTree(self):
    if self.root is not None:
      print('Tree is:')
      self._printTree(self.root)

  def _printTree(self,node):
    '''in-order traversal, switch print() for post-order or pre-order'''
    if node is not None:
      self._printTree(node.left)
      print(f'{node.v}')
      self._printTree(node.right)

tree=Tree()
while True:
  print("1.Add elements")
  print("2.Find elements")
  print("3.Print elements")
  print("4.Delete Tree")
  choice=int(input('\nEnter your choice:'))
  print()
  if choice==1:
    val=int(input('Enter an integer:'))
    tree.add(val)
  elif choice==2:
    val=int(input('Enter an integer:'))
    tree.find(val)
  elif choice==3:
    tree.printTree()
  elif choice==4:
    tree.deleteTree()
    break
  else:
    print("Wrong choice")
  print()
