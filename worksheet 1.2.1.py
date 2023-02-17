#1. WAP to check whether a a given number is a palindrome.

num = int(input("Enter an integer : "))
temp = num
rev = 0

while (num > 0):
    c = num % 10
    rev = rev * 10 + c
    num = num // 10

if (rev == temp):
    print(temp, " is a Palindrome")
else :
    print(temp, " is not a Palindrome")
