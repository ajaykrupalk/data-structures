'''Program to demonstrate sets'''
'''Some basic operations'''
set1=set([1,3,5,7,9])
set2=set([3,8,7,4,1])
set1.update(set2)
print("Updated set:",set1)#doesn't repeat data
set1.add(10)
set1.remove(3)
set1.pop()#removes element at first position
print("After some operations:",set1)
