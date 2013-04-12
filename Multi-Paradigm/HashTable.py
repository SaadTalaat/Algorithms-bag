from LinkedList import *
def hashx(key):
	return key
def destroyx(x):
	x = None
	return
def matchx(x,y):
	return x == y
class HashTable():
	buckets = 0
	hash_func = None
	match_func = None
	destroy_fun = None
	size = 0
	table = None

	def __init__(self,bucks, hasher, matcher,destroy):
		self.buckets 	= bucks
		self.hash_func	= hasher
		self.match_func	= matcher
		self.destroy_func	= destroy
		self.table = LinkedList();
		for i in range(0, self.buckets):
			self.table.attach(LinkedList())
		
		return

	def Table_destroy(self):
		for i in range(0,self.buckets):
			self.destroy(self.table.getElement())
		self.table = None
		return

	def Table_insert(self, value):
		to_insert = value
		x = self.Table_lookup(to_insert)
		if x == 0:
			return 1
		bucket = self.hash_func(value) % self.buckets

		self.table.get(bucket).attach(value)
		return

	def Table_remove(self, value):
		bucket = self.hash_func(value) % self.buckets
		self.table.get(bucket).delete(value)
		return

	def Table_lookup(self, value):
		bucket = self.hash_func(value) % self.buckets
		print "Bucket", bucket
		if not (self.table.get(bucket).isEmpty()):
			x = self.table.get(bucket).getvalue()
		else:
			return 1
		return 1

	def Table_size(self):
		return self.table.size()

table = HashTable(5,hashx,matchx,destroyx)
table.Table_insert(2)
table.Table_insert(2)
table.Table_insert(2)
