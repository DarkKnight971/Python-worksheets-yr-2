'''Write a Python program to replace last value of tuples in a list'''

t = 23, 29, 43, 59, 67
print("Original tuple : ", t)
t = list(t)

t[-1] = 97

t = tuple(t)
print("Updated tuple : ", t)
