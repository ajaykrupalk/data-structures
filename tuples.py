'''Program to demonstarte Tuples'''
'''List of tuples with given number and its cube'''
def cubes(list):
  result=[]
  for i in list:
    result.append((i,i**3))
  print(result)

cubes([7,5,4])
