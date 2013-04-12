def binarysearch(array,value):
	high = len(array)
	lo = 0
	while( lo <high):
		middle = (lo+high)/2
		if(array[middle] == value):
			return middle
		elif( array[middle] > value):
			high= middle
		elif( array[middle] < value):
			lo = middle+1
	return -1

array = [1,2,3,4,5,6,7]
print binarysearch(array, 7)
