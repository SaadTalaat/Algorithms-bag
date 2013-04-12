RED = 'red'
BLACK = 'black'

class RBT():
	root = None
	class Node():
		__left = None
		__right = None
		__value = None
		__key = None
		__color = None

		def __init__(self, key, value):
			self.__key = key
			self.__value = value
			self.__color = RED

		def getRight(self):
			return self.__right
		def setRight(self, node):
			assert node
			self.__right = node

		def getLeft(self):
			return self.__left
		def setLeft(self, node):
			assert node
			self.__left = node

		def setKey(self, key):
			assert key
			self.__key = key
		def getKey(self):
			return self.__key

		def getValue(self):
			return self.__value
		def setValue(self, val):
			assert val
			self.__value = val

		def isRed(self):
			return self.__color == RED
		def setColor(self, color):
			assert color
			self.__color = color

	def Put(self, key, value):
		self.put(self.root, key, value)

	def put(self, parent, key, value):
		if(parent == None):
			return Node(key, value)

		if parent.getKey() > key:
			parent.setLeft(self.put(parent.getLeft(), key, value))
		elif parent.getKey() < key:
			parent.setRight(self.put(parent.getRight(), key, value))
		else:
			parent.setValue(value)
		return

	def Get(self, key, value):
		return self.get(self.root, key)

	def get(self, parent ,key):
		if(parent == None):
			return None

		if(parent.getKey() < key):
			return self.get(parent.getRight, key, value)

		elif(parent.getKey() > key):
			return self.get(parent.setLeft, key, value)
		else:
			return parent.getValue()

	def RotateLeft(self, h):
		assert h.getRight().isRed()
		x = h.getRight()
		y = x.getLeft()
		x.setLeft(h)
		h.setRight(y)
		x.setColor(h.Color())
		h.setColor(RED)

	def RotateRight(self, node):
		assert node.getLeft().isRed()
		x = node.getLeft()
		y = x.getRight()
		node.setLeft(y)
		x.setRight(node)
		x.setColor(node.Color())
		h.setColor(RED)

	
