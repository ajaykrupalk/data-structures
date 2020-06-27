'''Program to demonstrate lists and list comprehension'''
'''Segregating 0's and 1's'''
def segregate(list):
 value=[x for x in list if x==0]+[x for x in list if x==1]
 print(value)

segregate([1,1,0,0,1,1,1,0,0,0])
