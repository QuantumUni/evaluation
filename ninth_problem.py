# In this problem I am going to solve a system of linear equations
import numpy as np
from scipy import linalg

if __name__ == "__main__":
	Coeffs = np.array([[1,2],[3,5]])
	vals = np.array([1,2])
	solutions = linalg.solve(Coeffs, vals)
	print(solutions)

