class Cell():
	'''
	Cell inside sorted linked list
	'''
	def __init__(self, value=None, next=None):
		self.value = value
		if (next) and (self.value > next.value):
			raise NextCellException("Next cell's value cannot be less than this cell's value.")
		self._next = next
		
	def __str__(self):
		return str(self.value)

	@property
	def next(self):
		return self._next
		
	@next.setter
	def next(self, next):
		if self.value > next.value:
			raise NextCellException("Next cell's value cannot be less than this cell's value.")
		self._next = next
	
def display(head):
	'''
	Output linked list starting from head.
	'''
	while (head):
		print(head)
		head = head.next

def insert(new_cell, head):
	before = head
	while before and before.next.value < new_cell.value:
		before = before.next
	new_cell.next = before.next
	before.next = new_cell

def remove(target, head):
	before = head
	while (before.next.value < target.value):
		before = before.next
	if (before.next.value == target.value):
		before.next = before.next.next
	
class NextCellException(Exception):
	pass

if __name__ == "__main__":
	#Initialize linked list
	c10 = Cell(10)
	c20 = Cell(20)
	c30 = Cell(30)
	c40 = Cell(40)
	c50 = Cell(50)
	
	c10.next = c20
	c20.next = c30
	c30.next = c40
	c40.next = c50
	
