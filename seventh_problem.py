# In this problem I am going to count the number of a unique word in a file
if __name__ == "__main__":
	fileAdd = input("Enter File Address: ")
	with open(fileAdd, 'r') as file:
		wordsList = file.read().split()
		# Remember in the sets, a value can not be repeated
		uniqueWords = set(wordsList)
		print(f"Number of Unique Words: {len(uniqueWords)}")
