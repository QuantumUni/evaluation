# In this problem I am going to get a comma separated sequence and sort them alphabatically
if __name__ == "__main__":
	sequence = input("Enter your sequence of words: ")
	sequence = sequence.split(',')
	sequence.sort()
	print(", ".join(sequence))
