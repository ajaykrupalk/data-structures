import array as arr#array module can represent an array of basic values
a=arr.array('i',[1,2,3,4,5])#array of integer values
while True:
  print("1. Add Elements")
  print("2. Delete Elements")
  print("3. Print Array")
  print("4. Exit")
  choice=int(input('Enter your choice:'))
  if choice==3:#to print elements
    print("\nThe array elements are:")
    for numbers in a:
      print(numbers,end=" ")
    print("\n")
  elif choice==1:#to add elements
    val=int(input('\nEnter an integer:'))
    print()
    a.append(val)
  elif choice==2:#to delete elements
    value=a.pop()
    print(f"\nPopped Value is: {value}\n")
  elif choice==4:
    print("\nEnd Of Program")
    break
  else:
    print("Invalid Choice")
