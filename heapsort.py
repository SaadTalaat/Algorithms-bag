class HeapSort():
	def parent(self, k):
		return k/2
	def left(self, k):
		return k*2
	def right(self, k):
		return (k*2)+1


	def sink(self, array, start, size):
		root = start
		while ( (root*2) +1 <= size):
			child = root*2 +1
			if (child + 1 <= size) and (array[(child+1)] > array[child]):

				child +=1
			if(child <= size) and ( array[child] > array[root]):
				array[root],array[child] = array[child],array[root]
				root = child
			else:
				return
	def heapify(self, array):
		init = (len(array)/2) -1
		while init >=0:
			self.sink(array, init, len(array) -1)
			init -=1

	def sort(self, array):
		self.heapify(array)
		n = len(array)-1
		while( n > 1):
			array[1],array[n] = array[n], array[1]
			n-=1
			self.sink(array, 1, n)
		
array = [1,2,3,4,5,6,7,8]
heap = HeapSort()
heap.heapify(array)
print array
heap.sort(array)
print array
