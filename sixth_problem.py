# In this program I am going to count number of lines in a text file

if __name__ == "__main__":
	fAddress = input("Enter File Address & Name: ")
	fn = open(fAddress,"r")
	lineCounter = 0
	for line in fn:
		lineCounter += 1
	# We can do this also in the following was
	lc = 0
	with open(fAddress,'r') as file:
		lc = len(file.readlines())
	print(f"Lines: {lineCounter}")
	print(f"Lines: {lc} (Second Method)")
