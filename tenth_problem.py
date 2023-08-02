# In this problem I am going to create.... Well the question is a ambiguous
# I will write different types of class
class Rectangle:
	def __init__(self,width,length):
		self.width = width
		self.length = length
	
	def area(self):
		return self.width*self.length

	def perimeter(self):
		return 2*self.width+2*self.length

# My second understanding of question
class Rectangle2:
	def __init__(self, width, length):
		self.width = width
		self.length = length
	
	def set_area(self):
		self._area = self.width*self.length
	def get_area(self):
		return self._area

	def set_perimeter(self):
		self._perimeter = self.width*2+self.length
	def get_perimeter(self):
		return self._perimeter
	
