#2.	Python program to implement bubble sort.

l1 = [10, 8, 4, 9, 11]
print(l1)
n = len(l1)

for i in range(n) :
    for j in range(n - i -1) :
        if l1[j] > l1[j + 1] :
            t = l1[j]
            l1[j] = l1[j + 1]
            l1[j + 1] = t

print(l1)
