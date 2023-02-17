#3.	WAP to Take three numbers from the user and print the greatest number

a = int(input("Enter an integer : "))
b = int(input("Enter an integer : "))
c = int(input("Enter an integer : "))

if (a > b):
    if (a > c):
        print("\Largest no. among the three : ", a)
    else :
        print("\nLargest no. among the three : ", c)
else :
    if (b > c):
        print("\nLargest no. among the three : ", b)
    else :
        print("\nLargest no. among the three : ", c)
