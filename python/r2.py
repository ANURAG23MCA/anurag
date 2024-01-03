class Rectangle:
	def __init__(self, length, width):
		self._length = length # Private attribute
		self._width = width # Private attribute
	def area(self):
		return self._length * self._width
	def __lt__(self, other):
		return self.area() < other.area()
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(4, 10)
if rectangle1 < rectangle2:
	print("Area of Rectangle 1 is smaller than the area of Rectangle 2.")
elif rectangle1 > rectangle2:
	print("Area of Rectangle 1 is larger than the area of Rectangle 2.")
else:
	print("Both rectangles have the same area.")
