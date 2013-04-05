def partition(array, low, high):
	if( low >= high):
		return
	i = low
	j = high
	pivot = low

	while True:
		i+=1
		while(array[i] < array[pivot]):
			i+=1
			if( i >= high):
				break
		while(array[j] > array[pivot]):
			j-=1
			if j <= low:
				break
		if( i >= j):
			break
		array[j],array[i] = array[i],array[j]
	array[j],array[pivot] = array[pivot],array[j]
	return j

def quicksort(array, low, high):
	if(low >= high):
		return
	p = partition(array, low, high)
	quicksort(array, low, p-1)
	quicksort(array, p+1, high)

def Quicksort(array):
	quicksort(array, 0, len(array)-1)


array = [1,5,6,2,9,3]

Quicksort(array)
print array
