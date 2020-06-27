class Stack:
  def __init__(self):
    self.items=[]#to store elements
  def is_empty(self):
    return self.items==[]#returns 'True' if empty 
  def push(self,ele):
    self.items.append(ele)#adding elements to stack
  def pop(self):
    return self.items.pop()#pops elements

s=Stack()
while True:
  print('1.Push')
  print('2.Pop')
  print('3.Quit')
  choice=int(input('Enter your choice:'))
  print()
  if choice==1:
    val=input('Enter a value:')
    s.push(val)
  elif choice==2:
    if s.is_empty():
      print("Stack is  empty")
    else:
      print("Popped value is:",s.pop())
  elif choice==3:
    break
  print()
