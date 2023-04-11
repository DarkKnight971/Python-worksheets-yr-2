'''Write a Python program to convert a tuple of
   string values to a tuple of integer values'''

t = '1', '2', '3', '4', '5'
print("Original tuple : ", t)

t = [int(i) for i in t]
t = tuple(t)

print("Updated tuple : ", t)
