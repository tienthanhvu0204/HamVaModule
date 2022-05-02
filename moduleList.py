def addItem (list, item):
  __doc__ = "Thêm item vào list"
  list.append (item)
  print (list)

def findItem (list, itemName):
  result = -1
  for i in range (len (list)):
    if list[i] == itemName:
      result = i
  return result

def removeItem (list, itemName):
  if findItem (list, itemName) == -1:
    print (itemName, "not in list")
  else:
    del list [findItem (list, itemName)]
list = list (input ())
print (list)
item = input ()

removeItem (list, item)
print (list)

