'''3. Write a Python class named Rectangle constructed by a
      length and width and a method which will compute the
      area of a rectangle'''

class Rectangle:
	def __init__(self, l, b) :
		self.l = l
		self.b = b
		
	def area(self) :
		return (self.l * self.b)
	
if __name__ == "__main__" :
	l = int(input("Enter length of rectangle : "))
	b = int(input("Enter breadth of rectangle : "))
	
	rect = Rectangle(l, b)
	print(f"Area of rectangle : {rect.area()}")
