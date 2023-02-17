#2. WAP to check Whether entered number is Armstrong or Not?

num = int(input("Enter an integer : "))
temp = num
arm = 0

while (num > 0):
    div = num % 10
    arm = arm + div ** 3
    num = n um// 10

if (arm == temp):
    print(temp, " is an Armstrong")
else :
    print(temp, " is not an Armstrong")
