#development release
def is_prime(number):
	'''
	Check whether the input number is a prime number
	using Fermat's Little Theorem
	Please advise...
	'''
	success = 0
	for i in range(1,number):	
		print((i^(number-1)) % number)
		if (((i^(number-1)) % number) == 1):
			success += 1
			
	#return chance if number is prime
	print(success)
	return 1 - (1/(2**success))
	