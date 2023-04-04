'''1.	Write a Python program to get a list, sorted in increasing
   order by the last element in each tuple from a given list of 
   non-empty tuples'''

# get the last key.
def last(n):
	return n[m]

# function to sort the tuple
def sort(tuples):

	# We pass user defined function last
	# as a parameter.
	return sorted(tuples, key = last)

# __main__ code
a = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
m = 2
print("Sorted : "),
print(sort(a))
