import numpy as np

def rectangle_rule(xmin, xmax, func, n):
	'''
	Calculate the area of func(x) between xmin and xmax
	using rectangle rule.
	'''
	dx = (xmax - xmin) / n
	total_area = 0
	
	for x in np.arange(xmin, xmax-dx, dx):
		total_area = total_area + func(x)
		
	total_area = total_area * dx
	
	return total_area
	
def trapezoid_rule(xmin, xmax, func, n):
	'''
	Calculate the area of func(x) between xmin and xmax
	using trapezoid rule.
	'''
	dx = (xmax - xmin) / n
	total_area = 0
	
	for x in np.arange(xmin, xmax, dx):
		total_area = total_area + func(x)
		
	total_area = total_area * 2 - func(xmin) - func(xmax)
	total_area = total_area * dx/2
	
	return total_area