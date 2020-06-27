'''Using dictionary to calculate the occurrances of the characters of a string'''
def calculate(string):
  result={}
  for key in string:
    if key not in result:
      result[key]=0
    result[key]+=1
  return result

print(calculate("programming"))
