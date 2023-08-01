# In this problem we are going to solve the first two problems using while and compare the execution time
# For this purpose we first import another module named time
# Remember time.time() returns seconds so the difference is in seconds unit
import time
count = 0
sum = 0
forStartTime = time.time()
for i in range(10):
	count += 1 if i%2==0 else 0
forRunTime = time.time()-forStartTime
counter = 0 
count = 0
whileStart = time.time()
while counter<10:
	count += 1 if i%2==0 else 0
	counter += 1
whileRunTime = time.time()-whileStart
print("For First Problem \n")
if whileRunTime>forRunTime:
	print(f"While Run Time:{whileRunTime} > For Run Time: {forRunTime}")
else:
	print(f"For Run Time: {forRunTime} > While Run Time: {whileRunTime}")
forStart = time.time()
for i in range(100,200):
	sum += i	
forRunTime = time.time()-forStart
counter = 100
sum = 0
whileStart = time.time()
while counter<200:
	sum += counter
	counter += 1
whileRunTime = time.time()-whileStart
print("For Second Problem:\n")
if whileRunTime > forRunTime:
	print(f"While Run Time: {whileRunTime} > For Run Time: {forRunTime}")
else:
	print(f"For Run Time: {forRunTime} > While Run Time: {whileRunTime}")

