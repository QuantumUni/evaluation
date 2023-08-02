# In this problem I am going to implement stack data structure in python
class Stack:
	def __init__(self, length):
		self._length = length
		self._items = ['']*length
		self._count = 0

	def __str__(self):
		test = self._items[0:self._count]
		string = "".join(str(test))
		return string

	def get_count(self):
		return self._count
	def set_count(self, val):
		self._count = val


	def  push(self, item):
		count = self.get_count()
		if count>=self._length:
			print("Stack is already full")
			return
		self._items[count] = item
		count+=1
		self.set_count(count)
	
	
	def pop(self):
		count = self.get_count()
		if count==0:
			print("Stack is already Empty")
			return
		item = self._items[count-1]
		count -= 1
		self.set_count(count)
		return item
	
	def traverse(self):
		count = self.get_count()
		if count==0:
			return
		items = self._items
		while(count > 0):
			count -= 1
			print(items[count])
		self.set_count(count)

if __name__ == "__main__":
	stack = Stack(5)
	stack.push("hdi")
	stack.push("ill")
	stack.push("lye")
	stack.push("niwla")
	stack.push("Bye")
	stack.push("Check")
	print(stack)
	stack.traverse()
	stack.pop()
	
