#2. Python program to find uncommon words from two Strings

a = input("Enter first string : ")
b = input("Enter second string : ")

a = a.split()
b = b.split()
c = []

for x in a :
  if x not in b :
    c.append(x)
for x in b :
  if x not in a :
    c.append(x)
    
print("Uncommon words : ", c)
