
class RBTree():
	class Node():
		__value = None
		__key   = None
		__left  = None
		__right = None
		__color = None
		def __init__(self, key, value):
			self.__key = key
			self.__value = value
			self.__color = 'red'
		def getKey(self):
			return self.__key

		def getValue(self):
			return self.__value

		def getRight(self):
			return self.__right
		def setRight(self,right):
			self.__right = right

		def getLeft(self):
			return self.__left
		def setLeft(self, left):
			self.__left = left
		def isRed(self):
			return self.color == 'red'
		def Red(self):
			self.color = 'red'
		def getColor(self):
			return self.color
		def setColor(self, col):
			self.color = col
	root = None
	def isRed(self, node):
		return node.isRed()
	def RotateLeft(self, h):
		assert h.getRight().isRed()
		x = h.getRight()
		y = x.getLeft()
		x.setLeft(h)
		h.setRight(y)
		x.setColor(h.getColor())
		h.Red()

	def RotateRight(self, h):
		assert h.getLeft().isRed()
		x = h.getLeft()
		h.setLeft(x.getRight())
		x.setRight(h)
		x.setColor(h.getColor())
		h.Red()

	def FlipColor(self, h):
		assert not h.isRed()
		assert h.getLeft().isRed()
		assert h.getRight().isRed()

	def Put(self, key, value):
		return self.put(self.root, key, value)
	
	def put(self, parent, key, value):
		if(parent == None):
			return self.Node(key,value)
		if(parent.getKey() > key):
			parent.setLeft(self.put(parent.getLeft(), key, value))

		if(parent.getKey() < key):
			parent.setRight(self.put(parent.getRight(), key, value))
		else:
			parent.setValue(value)
		if( parent.getRight().isRed()) and (not (parent.getLeft().isRed())):
				self.RotateLeft(parent)
		if( parent.getRight().isRed) and (parent.getLeft().getLeft().isRed()):
				self.RotateRight(parent)
		if( parent.getRight().isRed()) and ( parent.getLeft().isRed() ):
				self.FlipColors(parent)
		return parent

	def Inorder(self):
		node = self.root
		l = []
		self.inorder(node, l)
		return l
	def inorder(self, node , l):
		if node == None:
			return
		self.inorder(node.getLeft(), l)
		l.append(node.getKey())
		self.inorder(node.getRight(), l)
		return l


rb = RBTree()
print rb.Put(1,2).getKey()
print rb.Put(2,2).getKey()
print rb.Put(3,2).getKey()
print rb.Put(4,2).getKey()
print rb.Put(9,2).getKey()
print rb.Put(12,2).getKey()
print rb.Put(7,2).getKey()
