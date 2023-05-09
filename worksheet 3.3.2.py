'''2. Write a Python program to create a file where all
      letters of English alphabet are listed by specified
      number of letters on each line.'''
import string

l1 = list(string.ascii_lowercase)
l = len(l1)

with open('solution.txt', 'w+') as f :
	for i in range(l) :
		f.write(f'{l1[i]} - {(i+1)}\n')
	f.seek(0)
	f.read()
	f.close()
