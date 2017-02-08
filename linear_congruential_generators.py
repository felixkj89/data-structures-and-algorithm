def generate_lcg(start_value, a, b, m):
	'''
	Generate a list of random value.
	It satisfies periodic random value only if:
	1. b and m are relatively prime
	2. a-1 is divisible by all prime factors of m
	3. a-1 is a multiple of 4 if m is
	'''
	random_list = []
	x = start_value
	while True:
		random_list.append(x)
		x = (x * a + b) % m
		if x == start_value:
			break
	return random_list
	