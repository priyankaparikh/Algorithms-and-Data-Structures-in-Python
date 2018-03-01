class Node(object):

    def __init__(self, data):
    	self.data = data  # store the data
    	self.nextNode = None # store the reference to the nextnode

class LinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0   # initialize the size of the head an the list

	def insert_at_start(self, data):

		self.size = self.size + 1 # increment the size of the list
		newNode = Node(data) # instantiate a new node

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head # The newnode now points to the head
			self.head = newNode

	def size(self):
		return self.size

	def size2(self):
		"""iterate throught the list and return the size (01^)""" 
		currentNode = self.head
		size = 0

		while currentNode is not None:
			size += 1
			currentNode = currentNode.nextNode

		return size

	def insert_end(self, data):

		self.size = self.size + 1
		newNode = Node(data) # instantiate a new node with the data
		currentNode = self.head

		while currentNode.nextNode is not None:
			currentNode = currentNode.nextNode # Traverse in the whole list 

		currentNode.nextNode = newNode

	def traverse_list(self):

		currentNode = self.head

		while currentNode is not None:
			print(currentNode.data)
			currentNode = currentNode.nextNode

	def remove(self, data):

		if self.head is None:
			return

		self.size = self.size - 1
		currentNode = self.head
		previousNode = None # at the begining

		while currentNode.data != data: #check for data 
			previousNode = currentNode 
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode #update the refernce

		else:
			previousNode.nextNode = currentNode.nextNode

	def __str__(self):
		return self


LinkedList = LinkedList()

LinkedList.insert_at_start(19)
LinkedList.insert_at_start(31)
LinkedList.insert_at_start(90)
LinkedList.insert_end(96)



