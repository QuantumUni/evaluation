# In this problem I am going to write a recursive function to calculate the factorial of a number
def factorial(num):
	if(num>1):
		return num * factorial(num-1)
	else:
		return num

if __name__ == "__main__":
	number = int(input("Enter a number: "))
	print(factorial(number))
