from codes.find_prime import find_prime

def test_find_prime_1():
	assert [1] == find_prime(1)
	
def test_find_prime_2():
	assert [1, 2] == find_prime(2)

def test_find_prime_3():
	assert [1, 2, 3] == find_prime(3)
	
def test_find_prime_5():
	assert [1, 2, 3, 5] == find_prime(5)
	
def test_find_prime_10():
	assert [1, 2, 3, 5, 7] == find_prime(10)
	