#stacks can be easily implemented using arrays/linkedlist

class Stack:

	def __init__(self):
		self.Stack = [] # the stack is a one dimensional array

	def isEmpty(self):
		return self.Stack == []

	def push(self,data):
		# inserting items into self.stack
		self.Stack.append(data)

	def pop(self):
		# first item in last out
		data = self.Stack[-1]
		del self.Stack[-1]
		return data

	def peek(self):
		# returns the last inserted item 
		return self.Stack[-1]

	def sizeStack(self):
		return len(self.Stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.sizeStack())
print("popped :", stack.pop())
print("popped :", stack.pop())
print(stack.sizeStack())
print("peek :",stack.peek())