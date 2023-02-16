#3.	Write a  program to enter length in centimeter and convert it into meter and kilometer, and also convert the same into Equivalents 

cm1 = eval(input("Enter length(in cm) : "))

m1 = cm1 / 100
km1 = m1 / 1000

print("Converted lengths :", m1, "m & ", km1, "km \n")

m2= eval(input("Enter length(in m) : "))

cm2 = m2 * 100
km2 = m2 / 1000

print("Converted lengths :", cm2, "cm & ", km2, "km \n")

km3 = eval(input("Enter length(in km) : "))

m3 = km3 * 1000
cm3 = m3 * 100

print("Converted lengths :", m3, "m & ", cm3, "cm")
