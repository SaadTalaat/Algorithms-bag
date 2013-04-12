
def hasher(key):
	return key;
class HTable():
	size = 0
	buckets = 0
	hasher = None
	table = []
	def __init__(self, bucketz, hash_er):
		self.buckets = bucketz
		self.hasher = hash_er
		for i in range(0, self.buckets):
			self.table.append([])

	def insert(self, key):
		n = self.hasher(key) % self.buckets
		self.table[n].append(key)
		return self.table

	def remove(self, key):
		n = self.hasher(key) % self.buckets
		self.table[n].pop()
		return self.table

	def traverse(self, table, l):
		for i in range(0,len(table)):
			try:
				self.traverse(table[i])
				l.append(table[i])
				print "Here"
			except TypeError:
				l.append(table[i])
	def Traverse(self):
		l = []
		self.traverse(self.table , l)
		return l

ht = HTable(10, hasher)
ht.insert(0)
ht.insert(1)
ht.insert(2)
ht.insert(3)
ht.insert(4)
ht.insert(1)
print ht.Traverse()
