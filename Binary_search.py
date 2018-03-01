class Node(object):
	""" defines an object of the node class """

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinarSearchTree(object):
 	""" defines the class of the BinarSearchTree """

 	def __init__(self,):
 		self.root = None


 	def insertNode(self, data, node):
 		""" evaluates the data against the current node which is
 		passed into the function """

 		if data < node.data:
 			if node.left:
 				#calling the insertNode function recursively
 			   	self.insertNode(data, node.left)
 			else:
 				node.left = Node(data)
 		else:
 			if node.right:
 				#calling the insertNode function recursively
 				self.insertNode(data, node.right)
 			else:
 				node.right = Node(data)


 	def insert(self, data):
 		""" Insert a Node anywhere in the bst or create the root
 		"""

 		if not self.root:
 			self.root = Node(data)
 		else:
 			self.insertNode(data, self.root)


 	def getMinValue(self):
 		""" returns the minimum value in a BST """

 		if self.root:
 			#calls itself recursively
 			return self.getMinValue(self, root)


 	def getMin(self, node):
 		""" evaluates the if the current node has a leftCHild """

 		# keep calling getMin with the node.left recursively till
		# if statement is no longer true
 		if node.leftChild:
 			return self.getMin(node.leftChild)

 		return node.data


 	def getMaxValue(self):
 		""" returns the max value in a BST"""
 		if self.root:
 			return self.getMax(self, root)


 	def getMax(self, Node):
 		""" evaluates if a node has a right"""
 		if node.rightChild:
 			return self.getMax(node.rightChild)

 		return node.data

 	def Traverse(self):
 		""" Traverse a Binary Search Tree"""
 		if self.root:
 			self.TraverseInOrder(self.root)

 	def TraverseInOrder(self, node):
 		""" Traverse and display the nodes """
 		if node.left:
 			self.TraverseInOrder(node.left)
			print "Current Node : {}".format(node.data)
 			if node.right:
 			self.TraverseInOrder(node.rightChild)

	def remove(self, data):
		""" remove data"""

		if self.root:
			return self.removeNode(Self, data):

	def removeNode(self, data, node):

		if not node:
			return node

		if data < node.data:
			node.leftChild
		elif datd > node.data:
