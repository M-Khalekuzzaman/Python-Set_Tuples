#Set is a unorder collection of item
num1 = {1,2,3,4,5,}
num2 = set([4,5,6,7])

print(num1 | num2)   #Union set function
print(num1 & num2)    #intersection  set function
print(num1 - num2)     #Difirecnce sset function



num1 = {1,2,3,4,5,}
num2 = set([4,5,6,7])
num2.add(8)
num1.remove(5)
print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
