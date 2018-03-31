""" AVL trees Implementation.
- Always balance the tree.
- Check for the height parameters every time a rotation is done.
- A null has a height parameter of -1.
- A leaf node has a height parameter of 0.
- the difference between a left_child and right_child must not exceed 1.
- The above formula must be applied to all the nodes in the tree.
- Follow this formula for determining the height of a parentNode:
- Height = max(left_child.height(), right_child.height()) + 1
"""


class Node(object):

	def __init__(self, data):
		self.data = data
		self.height = 0;
		self.left_child = None
		self.right_child = None


class AVL(object):

	def __init__(self):
		self.root = None


	def insert(self, data):
		""" Inserting a node in an AVL tree:
			- Each insertion requires checking for any AVL tree property
			violations
		"""

		self.root = self.insertNode(data, self.root)


	def insertNode(self, data, node):
		""" inserts a new node in an AVL tree
		"""

		# if there is no head then make the head by instantiating
		# a new node
		if not node:
			return Node(data)

		# tell the parent that the left child or right child is updated
		if data < node.data:
			# recursively call the function on itself
			node.leftChild = self.insertNode(data, node.leftChild)

		else:
			node.rightChild = self.insertNode(data, node.rightChild)

		node.height = max(self.calc_height(node.leftChild),
							self.rightChild(node.rightChild)) + 1

		return self.settle_violation(data, node)


	def settle_violation(self, data, node):
		""" Checks the tree for an property violations """

		# this returns an integer value
		bal = self.calculate_balance(node)

		# case 1 : left left heavy situation, if it is known that the data is
		# less than the node.leftChild.data
		if bal > 1 and data < node.leftChild.data:
			print("this is a left left heavy situation")
			return self.rotate_right(node)

		# case 2 : right right heavy situation, if it is known that the data is
		# greater than the node.rightChild.data
		if bal < -1 and data > node.rightChild.data:
			print("this is a right right hevy situration")
			return self.rotate_left(node)

		# case3 : left right heavy situation
		if bal > 0 and data > node.leftChild.data:
			node.leftChild = self.rotate_left(node.leftChild)
			return self.rotate_right(node)

		# case4 : right left heavy situation
		if bal < -1 and data < node.rightChild.data:
			node.rightChild = self.rotate_right(node.rightChild)
			return self.rotate_left(node)


	def calc_height(self, node):
		""" calculates the height of a given node.
			This function is nessecary to make up for the value of None
		"""
		# if null
		if not node:
			return -1;
		# else return the given node's height value
		return node.height


	def calculate_balance(self, node):
		""" Check if the tree is balanced
		- If the function returns a value > 1 :
			then the tree is left heavy => do a right rotation
		- If the function returns a value < 1 :
			then the tree is right heavy => do a left rotation
		"""

		if not node:
			return 0

		return self.calc_height(node.left_child) - self.calc_height(node.right_child)


	def rotate_right(self, node):
		""" Rotates the tree to balance the tree.
		- The node is the head of the AVL tree.
		- Initialize two variables
		- Reassigning the variables
		"""

		print (node.data)

		# Initialize a temporary leftChild to hold the curent node's lc
		temp_lc = node.leftChild
		# Initialize a new variable t to store the temp_lc's rightChild
		t = temp_lc.rightChild
		# Making the temp_lc now the head.
		temp_lc.rightChild = node
		# Making the head's leftChild == t
		node.leftChild = t

		# After reassigning the variables update the height
		node.height = max(self.calc_height(node.leftChild,
						self.calc_height(node.rightChild))) + 1

		temp_lc.height = max(self.calc_height(node.leftChild,
						self.calc_height(node.rightChild))) + 1

		# return the root node
		return temp_lc


	def rotate_left(self, node):
		""" Rotates the tree to balance the tree.
		- The node is the head of the AVL tree.
		- Initialize two variables
		- Reassigning the variables

		Rotations are very fast:
		- They have o(1) time complexity
			- Because reassigning a reference variable is o(1)
			- The height is also being thracked that is o(1)
		"""

		# Initialize a temporary rightChild to hold the curent node's rc
		temp_rc = node.rightChild
		# Initialize a new variable t to store the temp_lc's rightChild
		t = temp_rc.leftChild
		# Making the temp_lc now the head.
		temp_rc.leftChild = node
		# Making the head's leftChild == t
		node.rightChild = t

		# After reassigning the variables update the height
		node.height = max(self.calc_height(node.leftChild,
						self.calc_height(node.rightChild))) + 1

		temp_rc.height = max(self.calc_height(node.leftChild,
						self.calc_height(node.rightChild))) + 1

		# return the root node
		return temp_rc
