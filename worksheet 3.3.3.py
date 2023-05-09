#3. Write a Python program to read a random line from a file.
import random
import string

l1 = list(string.ascii_lowercase)
l = len(l1)

with open('solution.txt', 'w+') as f :
	for i in range(l) :
		f.write(f'{l1[i]} - {(i+1)}\n')
	f.seek(0)
	l2 = f.read().splitlines()
	print(random.choice(l2))
	f.close()
