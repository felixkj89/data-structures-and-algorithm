from codes.factorize import factorize

def test_factorize_1():
	assert [1] == factorize(1)
	
def test_factorize_2():
	assert [2] == factorize(2)

def test_factorize_3():
	assert [3] == factorize(3)
	
def test_factorize_4():
	assert [2, 2] == factorize(4)
	
def test_factorize_5():
	assert [5] == factorize(5)
	
def test_factorize_100():
	assert [2, 2, 5, 5] == factorize(100)


