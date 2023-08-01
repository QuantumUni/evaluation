#This program is going to count the even numbers between 0 and 10
#It uses for loop
evenNumbers = 0
#Remember this does not count the upper limit
#If you want to count 10 also you need to set upper limit to 11
for i in range(10):

	# I am using ternary operator
	evenNumbers += 1 if i%2==0 else 0

print(evenNumbers)
