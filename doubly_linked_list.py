class Cell():
	'''
	Cell inside doubly linked list
	'''
	def __init__(self, value=None, previous=None, next=None):
		self.value = value
		self.previous = previous
		self.next = next
		
	def __str__(self):
		return str(self.value)

	def add_after(self, new_cell):
		new_cell.next = self.next
		new_cell.previous = self
		
		self.next = new_cell
		new_cell.next.previous = new_cell
		
	def remove(self):
		self.next.previous = self.previous
		self.previous.next = self.next
		

def display(member):
	while (member.previous):
		member = member.previous
		
	while (member):
		print(member)
		member = member.next
	
if __name__ == "__main__":
	#Initialize linked list
	c10 = Cell(10)
	c20 = Cell(20)
	c30 = Cell(30)
	c40 = Cell(40)
	c50 = Cell(50)
	
	c10.next = c20
	c20.previous = c10
	c20.next = c30
	c30.previous = c20
	c30.next = c40
	c40.previous = c30
	c40.next = c50
	c50.previous = c40
		
		
		