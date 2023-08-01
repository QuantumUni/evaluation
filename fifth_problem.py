# In this problem I am going to compare runtime of my factorial (recursive) and built-in math factorial function
import timethis
from forth_problem import factorial
import math
number = int(input("Enter a number: "))
myFuncRT, myFuncRes = timethis.timeThis(factorial,number)
mathFuncRT, mathFuncRes = timethis.timeThis(math.factorial,number)
print(f"My Result: {myFuncRes}\t Math Result: {mathFuncRes}")
if(myFuncRT>mathFuncRT):
	print(f"My Function Run Time: {myFuncRT} > Math Function Run Time: {mathFuncRT}")
else:
	print(f"Math Function Run Time: {mathFuncRT} > My Function Run Time: {myFuncRT}")
