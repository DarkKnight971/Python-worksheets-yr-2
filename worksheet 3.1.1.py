#1.	Python program to implement linear search.

l1 = [10, 4, 8, 4, 9, 11]
print(l1)

s = int(input("Enter number to search : "))
c = 0
d = 0

for i in l1 :
    if i == s :
        c += 1
        print(s, " found at ", d)
    d += 1

if c == 0 :
    print(s, " not found")
