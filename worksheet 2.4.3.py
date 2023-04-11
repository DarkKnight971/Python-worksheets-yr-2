'''Write a Python program calculate the product,
   multiplying all the numbers of a given tuple.'''

t = 1, 2, 3, 4, 5, 6
print("Original tuple : ", t)

prod = 1
t = list(t)
for i in t :
   prod *= i

print("Product of elements of tuple : ", prod)
