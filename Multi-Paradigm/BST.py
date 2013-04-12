from Queue import *
class Bst():

	class Node():
		__key   = None
		__value = None
		__right = None
		__left  = None
		def __init__(self, key, value):
			self.__key = key
			self.__value = value

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
	root = None
	def Put(self, key, value):
		self.root = self.put(self.root,key,value)
		return self.root

	def put(self,parent ,key, value):
		if( parent == None):
			return self.Node(key,value)
		if(parent.getKey() < key):
			parent.setRight(self.put(parent.getRight(), key, value))
		elif(parent.getKey() > key):
			parent.setLeft(self.put(parent.getLeft(), key, value))
		else:
			parent.setValue(value);
		return parent

	def Get(self, key):
		return self.get(self.root, key);

	def get(self, parent, key):
		if(parent == None) or (key == None):
			return None

		if(parent.getKey() < key):
			return self.get(parent.getRight(), key)
		elif(parent.getKey() > key):

			return self.get(parent.getLeft(),key)
		else:
			return parent.getValue()
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

	def Preorder(self):
		l = []
		self.preorder(self.root, l)
		return l
	def preorder(self, parent, l):
		if parent == None:
			return
		l.append(parent.getKey())
		self.preorder(parent.getLeft(), l)
		self.preorder(parent.getRight(), l)

	def Postorder(self):
		l = []
		self.postorder(self.root, l)
		return l

	def postorder(self, parent, l):
		if(parent == None):
			return
		self.postorder(parent.getRight(), l)
		self.postorder(parent.getLeft(), l)
		l.append(parent.getKey())

	def Levelorder(self):
		l = []
		self.levelorder(self.root, l)
		return l

	def levelorder(self, parent, l):
		if(parent == None):
			return
		q = Queue()
		q.put(parent)
		while not q.empty():
			x = q.get()
			l.append(x.getKey())
			if x.getLeft() != None:
				q.put(x.getLeft())
			if x.getRight() != None:
				q.put(x.getRight())
		
			

	def Delete(self, key):
		self.delete(self.root, key)

	def delete(self, node, key):
		if(node == None):
			return
		if( node.getKey() > key):
			if(node.getLeft().getKey() == key):
				node.setLeft(None)
			else:
				self.delete(node.getLeft(), key)
		if( node.getKey() < key):
			if(node.getRight().getKey() == key):
				node.selfRight(None)
			else:
				self.delete(node.getRight(), key)
		return

b = Bst()
b.Put(6,333)
b.Put(2,22)
b.Put(8,222)
b.Put(4,2222)
b.Put(7,2222)
b.Put(1,2222)
print b.Inorder()
print b.Preorder()
print b.Postorder()
print b.Levelorder()
