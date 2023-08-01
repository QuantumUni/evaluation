# In this problem we are going to write a decorate function and compare runtime of our factorial function with math built in factorial function
import time
def timeThis(func,num):
	startTime = time.time()
	result = func(num)
	runTime = time.time()-startTime
	return runTime, result
