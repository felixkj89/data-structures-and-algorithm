def gcd(a,b):
	'''
	Greatest common divisor of a and b.
	'''
	while(b != 0):
		remainder = a%b
		a = b
		b = remainder
	return a

def lcm(a,b):
	'''
	Least common multiple of a and b.
	'''
	return (a*b)/gcd(a,b)