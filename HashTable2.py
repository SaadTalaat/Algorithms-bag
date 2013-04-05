def hasher(value):
	return value

class HTable():
	buckets = 0
	hasher = None
	matcher = None
	table = []
	size = 0

	def __init__(self, buckets, hasher):
		self.buckets = buckets
		self.hasher = hasher
		size = 0

		for i in range(0,buckets):
			self.table.append([])

	def insert(self, value):
		position = self.hasher(value) % self.buckets
		self.table[position].append(value)
	def get(self, value):
		position = self.hasher(value) % self.buckets
		return self.table[position].pop()
	def getTable(self):
		return self.table


t = HTable(20, hasher)
t.insert(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(5)
t.insert(6)
t.get(5)
print t.getTable()
