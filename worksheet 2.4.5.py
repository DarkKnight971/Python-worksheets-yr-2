'''Write a Python program to check if a
   specified element presents in a tuple of tuples'''

t = (23, 29), (41, 53), (67,79)
print("Original tuple : ", t)

s = int(input("Enter number to search : "))
l = []

for i in t :
   if s in i :
      l.append(s)

print("Element present" if l else "ELement absent")
