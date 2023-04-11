'''Write a Python program to remove an empty
   tuple(s) from a list of tuples'''

t = (), (23, 29), (43, 59, 67)
print("Original tuple : ", t)

t = list(t)
for i in t :
   if not i :
      t.remove(i)
t = tuple(t)

print("Updated tuple : ", t)
