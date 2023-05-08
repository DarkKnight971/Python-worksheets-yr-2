'''4. Write a Python class named Circle constructed by a
      radius and two methods which will compute the area
      and the perimeter of a circle'''

class Circle:
    def __init__(self, r) :
      self.r = r

    def area(self) :
      return (3.14 * self.r * self.r)
    
    def perimeter(self) :
      return (2 * 3.14 * self.r)
	
if __name__ == "__main__" :
    r = int(input("Enter radius of circle : "))

    c = Circle(r)
    print(f"\nArea of rectangle : {c.area()}")
    print(f"Perimeter of rectangle : {c.perimeter()}")
