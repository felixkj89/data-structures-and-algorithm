class Cell():
	'''
	Cell inside linked list
	'''
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next
		
	def __str__(self):
		return str(self.value)

def display(head):
	'''
	Output linked list starting from head.
	'''
	while (head):
		print(head)
		head = head.next

def insert_begin(new_cell, head):
	new_cell.next = head

def insert_middle(new_cell, to_cell, head):		
	before_cell = head
	while (head):
		before_cell = head
		head = head.next
		if head == to_cell:
			break
	new_cell.next = to_cell
	before_cell.next = new_cell

def insert_end(new_cell, head):
	while (head):
		if head.next == None:
			head.next = new_cell
			return
		head = head.next

if __name__ == "__main__":
	#Initialize linked list
	c1 = Cell(1)
	c2 = Cell(2)
	c3 = Cell(3)
	
	c1.next = c2
	c2.next = c3
	
	