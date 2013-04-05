from Queue import *
RED = 'red'
BLACK = 'black'

class BST():
	__root = None
	class Node():
		__value = None
		__key = None
		__left = None
		__right = None
		__color = None
		def getRight(self):
			return self.__right
		def setRight(self, node):
			assert node != None
			self.__right = node
		def getLeft(self):
			return self.__left
		def setLeft(self, node):
			assert node != None
			self.__left = node
		def getKey(self):
			return self.__key
		def setValue(self,val):
			self.__value = val
		def getValue(self, val):
			return self.__value
		def __init__(self, key, value):
			self.__key = key
			self.__value = value
			self.__color = RED
		def isRed(self):
			return self.__color == RED
		def setColor(self, color):
			self.__color = color

	def Put(self, key, value):
		self.__root = self.put(self.__root, key, value)

	def put(self, parent, key, value):
		if(parent == None):
			return self.Node(key, value)
		if( parent.getKey() > key):
			parent.setLeft(self.put(parent.getLeft(), key, value))
		elif( parent.getKey() < key):
			parent.setRight(self.put(parent.getRight(), key, value))
		else:
			parent.setValue(value)
		if( parent.getRight()) and (parent.getLeft()):
			if( parent.getRight().isRed()) and (not (parent.getLeft().isRed())):
					self.rotateLeft(parent)
			if( parent.getRight().isRed) and (parent.getLeft().getLeft()) and (parent.getLeft().getLeft().isRed()):
					self.rotateRight(parent)
			if( parent.getRight().isRed()) and ( parent.getLeft().isRed()):
					self.FlipColors(parent)
		return parent

	def Get(self, key):
		self.get(self.__root, key)

	def get(self, parent, key):
		if(parent == None):
			return
		if (parent.getKey() > key):
			return self.get(parent.getLeft(), key);
		elif (parent.getKey() < key):
			return self.get(parent.getRight(), key);
		else:
			return parent.getValue()
	def rotateLeft(self, parent):
		l = parent.getLeft()
		parent.setLeft(l.getLeft())
		l.setLeft(parent)
	def rotateRight(self, parent):
		r = parent.getRight()
		parent.setRight(r.getRight())
		l.setRight(parent)
	def FlipColors(self, parent):
		assert parent.isRed()
		assert parent.getLeft().isRed()
		assert parent.getRight().isRed()
		parent.setColor(RED)
		parent.getLeft().setColor(BLACK)
		parent.getRight().setColor(BLACK)
	
	def Inorder(self):
		node = self.__root
		l = []
		self.inorder(node, l)
		return l
	def inorder(self, parent, l):
		if (parent == None):
			return
		self.inorder(parent.getLeft(), l)
		l.append(parent.getKey())
		self.inorder(parent.getRight(), l)
	def levelOrder(self):
		l = []
		self.levelorder(self.__root, l)
		return l
	
	def levelorder(self, parent, l):
		if parent == None:
			return
		q = Queue()
		q.put(parent)
		while not (q.empty()):
			p = q.get()
			if(p == None):
				return
			l.append(p.getKey())
			if (p.getLeft()!= None):
				q.put(p.getLeft())
			if (p.getRight != None):
				q.put(p.getRight())


	def isEmpty(self):
		return self.__root == None

b = BST()
b.Put(1,2)
b.Put(5,5)
b.Put(2,6)
b.Put(6,7)
b.Put(7,99)
b.Put(4,22)
print b.Inorder()
print b.levelOrder()
