
# transC chuyển nhiệt độ F sang C
def transC (f):
    return (f - 32) / 1.8

# sort một chuỗi số
myString = [3, 1, 1]
j = 1
# def sortString (string):
#     myString = string
#     for i in range (len (myString)-1):
#         for j in range (len (myString) - i - 1):
#             if int (myString [j]) > int (myString [j + 1]):
tempmin = [myString [j + 1]]
tempmax = [myString [j]]
temp0 = [myString [0: j:]]
temp1 = [myString [j + 2::]]
string = temp0 + tempmin + tempmax + temp1
    
#     return myString
# a = [3, 2, 1]
print (string)