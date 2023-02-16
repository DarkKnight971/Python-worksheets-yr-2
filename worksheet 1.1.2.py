#2.	Write a  program to enter marks of five subjects and calculate total, average and percentage

m1 = eval(input("Enter marks of subject 1 : "))
m2 = eval(input("Enter marks of subject 2 : "))
m3 = eval(input("Enter marks of subject 3 : "))
m4 = eval(input("Enter marks of subject 4 : "))
m5 = eval(input("Enter marks of subject 5 : "))

total = m1 + m2 + m3 + m4 + m5
avg = total / 100
prcnt = (total / 500) * 100

print("\n")
print("Total marks obtained : ", total)
print("Average marks obtained : ", avg)
print("Percentage obatined : ", prcnt, "%")
