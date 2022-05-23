def addItem (list, item):
  __doc__ = "Thêm item vào list"
  # name = input ("Name: ",)
  cost = input ("Cost: ",)
  date = input ("Date: ",)
  tempItem = {'Name': item, 'Cost': cost, 'Date': date}
  list.append (tempItem)
  print ("Done.")

def findItem (list, itemName):
  result = -1
  for i in range (len (list)):
    if list[i]['Name'] == itemName:
      result = i
  return result

def removeItem (list, itemName):
  if findItem (list, itemName) == -1:
    print (itemName, "not in list.")
  else:
    del list [findItem (list, itemName)]
    print ("Done.")

# Tạo list rỗng, hỏi người dùng muốn thêm các mục chi tiêu không?
# Nếu trả lời n/N exit, y/Y add, else: print (invalid input)
expenditures = []
print ("Your expenditures is empty! Do you want to add some?")

while True:
    answer = input ("Y/N? ",)
    if answer == "N" or answer == "n":
        break
    elif answer == "y" or answer == "Y":
        option = "add"
        while answer == "y" or answer == "Y":
            numberItem = int (input ("How many expenditures? "))
            if option == "add":   
                for i in range (numberItem):
                    print ("Expenditure number " + str (i + 1))
                    item = input ("Name: ",)
                    addItem (expenditures, item)
                    print ("Your expenditures is added!")
            else:
                for i in range (numberItem):
                    item = input ("Expenditure number " + str (i + 1) + ": ",)
                    removeItem (expenditures, item)
                print ("Your expenditures is removed!")
            
            print ("Your expenditures:", expenditures)
            # Hỏi xem người dùng muốn thêm hay xoá item?
            # Hỏi cho đến khi trả lời đúng, y: hỏi tiếp đến khi dc option đúng rồi break, n: break
            while True:
                print ("Do you want to add or remove some?")
                answer = input ("Y/N? ",)
                if answer == "n" or answer == "N":
                    break
                elif answer == "y" or answer == "Y":
                    while answer == "y" or answer == "Y":
                        option = input ("add/remove? ",)
                        if option != "add" and option != "remove":
                            print ("Invalid input!")
                        else:
                            break
                    break
                else:
                    print ("Invalid input!")

        print ("Your expenditures:", expenditures)
        break
    else:
        print ("Invalid input!")
exit
