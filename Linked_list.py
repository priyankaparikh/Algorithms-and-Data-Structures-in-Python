class Node(object):
    """ Definition of a basic node for a Linkedlist. """

    def __init__(self, data):
        self.data = data  # store the data
        self.nextNode = None  # store the reference to the nextnode


class LinkedList(object):
    """ Definition for a linked list obj. """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0   # initialize the size of the head an the list

    def insert_at_start(self, data):
        """ Inserts a node at the start of a LinkedList. """

        self.size = self.size + 1 # increment the size of the list
        newNode = Node(data) # instantiate a new node

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head  # The newnode now points to the head
            self.head = newNode

    def size(self):
        """ Returns the sixe of a node."""
        return self.size

    def size2(self):
        """iterates through the list and returns the size (01^)"""

        currentNode = self.head
        size = 0

        while currentNode is not None:
            size += 1
            currentNode = currentNode.nextNode

        return size

    def insert_end(self, data):
        """ iterates through the lilnkedlist and add a node to the end"""

        self.size = self.size + 1
        newNode = Node(data) # instantiate a new node with the data
        currentNode = self.head

        while currentNode.nextNode is not None:
            # Traverse in the whole list
            currentNode = currentNode.nextNode

        currentNode.nextNode = newNode

	def traverse_list(self):
        """ Iterates through the entire list. """

        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

	def remove(self, data):
        """ Iterates recursively and removes a given node """

        if self.head is None:
            return

        # Adjust the size of the LinkedList
        self.size = self.size - 1
        curr = self.head
        prev = None # at the begining

        while curr.data != data:  # check for data
            prev = curr
            curr = curr.nextNode

        if prev is None:
	           self.head = curr.nextNode #update the reference

        else:
            prev.nextNode = curr.nextNode

    def __str__(self):
        return self


LinkedList = LinkedList()

LinkedList.insert_at_start(19)
LinkedList.insert_at_start(31)
LinkedList.insert_at_start(90)
LinkedList.insert_end(96)
