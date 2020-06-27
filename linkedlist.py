class Node(object):
  def __init__(self,data):
    self.data=data#to store element
    self.link=None#to store address of next element
  
class LinkedList(object):
  def __init__(self):
    self.head=None#to store the head

  def insert(self,data):
    new_node=Node(data)
    if self.head is None:
      self.head=new_node
      return
    current=self.head
    while current.link:#till the end of the linked list
      current=current.link#getting the address
    current.link=new_node#storing the new element

  def print(self):
    current=self.head
    while current:
      print(current.data)#prints the data
      current=current.link#gets the address

  def search(self,data):
    current=self.head
    found=False
    while current and found is False:
      if current.data==data:
        found=True
      else:
        current=current.link
    if current is None:
      raise ValueError("Data not in List")#if element not found
    return found
  
  def delete(self,data):
    current=self.head
    previous=None
    found=False
    while current and found is False:
      if current.data==data:
        found=True
      else:
        previous=current#to store the previous element
        current=current.link#to store the current element
    if current is None:
      raise ValueError("Data not in List")
    if previous is None:#if element in first position
      self.head=current.link
    else:#if element in any other position
      previous.link=current.link

    

trial=LinkedList()
trial.insert(1)
trial.insert(2)
trial.insert(3)
trial.print()
val=trial.search(1)
if val:
  print('Found')
trial.delete(1)
trial.print()
