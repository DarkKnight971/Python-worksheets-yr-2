#1. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

l1 = list(string.ascii_uppercase)
l = len(l1)

for i in range(l) :
	f = open(f'{l1[i]}.txt', 'x')
	f.close()
