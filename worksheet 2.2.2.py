'''2.	Write a Python program to print a specified list after
   removing the 0th, 4th and 5th elements, Sample List : 
   ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],
   Expected Output : ['Green', 'White', 'Black']'''

new_list = []
for index, value in enumerate(my_list):
    if index not in [0, 4, 5]:
        new_list.append(value)
print(new_list)
