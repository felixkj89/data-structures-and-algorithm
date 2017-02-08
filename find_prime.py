
def find_prime(end_number):
	'''
	Generate a list that produce prime number
	between 1 and end_number.
	'''
	#initialize array is_prime
	is_prime = [True for i in range(0,end_number)]
	
	#eliminate multiples of 2
	for i in range(3, end_number, 2):
		is_prime[i] = False
	
	for p in range(2, end_number, 2):
		#make sure p is prime
		if (is_prime[p]):
			#eliminate multiples of prime number
			for m in range(2*(p+1), end_number, p+1):
				if (p+1)^2 > end_number:
					break
				else:
					is_prime[m-1] = False
				
	#return list of prime numbers
	i = 0
	primes = []
	for i in range(0,end_number):
		if is_prime[i]:
			primes.append(i+1)
	return primes
