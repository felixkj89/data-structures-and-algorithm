from math import sqrt

def factorize(number):
	'''
	Produce a list that contains the factors
	of the input number.
	'''
	factors_list = []
	
	#factorize(1)
	if (number == 1):
		factors_list.append(1)
		return factors_list
	
	while (number % 2 == 0):
		factors_list.append(2)
		number = number/2
		
	factor = 3
	stop_at = sqrt(number)
	while (factor <= stop_at):	
		while (number%factor == 0):
			factors_list.append(factor)
			number = number/factor
			stop_at = sqrt(number)
		factor = factor + 2
		
	if (number > 1):
		factors_list.append(number)
	return factors_list