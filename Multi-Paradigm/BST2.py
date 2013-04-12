from Queue import *
import sys,random

class BST():
	__root = None
	__size = 0
	class Node():
		__value = None
		__key = None
		__left = None
		__right = None
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

	def Root(self):
		return self.__root
	def Put(self, key, value):
		self.__size+=1
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
	def Preorder(self):
		l = []
		self.preorder(self.__root, l);
		return l
	def preorder(self, parent, l):
		if(parent == None):
			return
		l.append(parent.getKey())
		self.preorder(parent.getRight(), l)
		self.preorder(parent.getLeft(), l)
	def printree(self):
		x = self.Preorder()
		prev = 1
		buf = ''
		for i in range(len(x)-1,0, -1):
			buf +='\t'*i
			buf += '%d' % x[len(x) - i]
			#print '\t'*i,x[len(x)-i]
			if ( i % prev) or prev == 1 :
				prev +=1
				print buf
				buf = ''

	def levelOrder(self):
		l = []
		self.levelorder(self.__root, l)
		return l	
	def levelorder(self, parent, l):
		indent = self.__size
		buf = ''
		cur = prev = pprev = 0
		if parent == None:
			return
		q = Queue()
		q.put(parent)
		while not (q.empty()):
			cur +=1
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


def get_Nth(parent, n):
	if(parent == None):
		return
	l = []
	Inorder(parent, l)
	assert l[n]
	return l[n]

def Inorder(root, l):
	if(root == None):
		return
	Inorder(root.getLeft(), l)
	l.append(root.getKey())
	Inorder(root.getRight(), l)

b = BST()
for i in range(0,50):
	b.Put(random.randint(0,800) , 0)
#print b.Inorder()
#print b.levelOrder()
arr =  b.Inorder()
print arr
arr =  b.Preorder()
print arr
cur =0
prev =0

def printx(prev, cur):

	print ""
	try:
		for i in range(prev, cur):
			sys.stdout.write("%d " % arr[i])
			if( (i % 2) == 1):
				sys.stdout.write(" ");
			elif( cur > 40):
				sys.stdout.write(" ");
	except:
		return;
	if(prev == cur):
		sys.stdout.write("%d " % arr[0])
		print ""
		sys.stdout.write("/\\")
		printx(prev, cur+2)
	else:
		prev = cur
		cur += cur +2
		print ""
		sys.stdout.write("/\\"*prev)
		printx(prev,cur)


def doit(c):
     level=1
     count=0
     for i in c:
            print i,
            count+=1
	    print level,
            if(count==level):
                print "\n"
                level*=2
                count=0

doit(arr)
