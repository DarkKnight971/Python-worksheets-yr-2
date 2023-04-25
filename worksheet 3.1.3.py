#3.	Python program to implement binary search without recursion.

l1 = [10, 8, 4, 9, 11]
l1.sort()

s = int(input("Enter number to search : "))

l = 0
u = len(l1) -1
m = (l + u) // 2
c = 0

while l < u :
    if s == m :
        print(s, "found at ", m)
        c += 1
        break
    elif s < m :
        u = m - 1
        m = (l + u) // 2
    elif s > m :
        l = m + 1
        m = (l + u) // 2

if c == 0 :
    print(s, " not found")
