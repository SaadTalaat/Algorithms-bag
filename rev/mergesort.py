def mergesort(array):
	if len(array) == 1:
		return array
	
	middle = len(array)/2
	left = mergesort(array[:middle])
	right = mergesort(array[middle:])

	if not len(left) or not len(right):
		return left or right
	result = []
	l = r = 0
	while( len(result) < (len(right) + len(left))):
		if left[l] < right[r]:
			result.append(left[l])
			l+=1
		elif right[r] < left[l]:
			result.append(right[r])
			r+=1
		while( l == len(left) and r < len(right)):
			result.append(right[r])
			r+=1
		while( r == len(right) and l < len(left)):
			result.append(left[l])
			l+=1
	return result


array = [2,5,1,9,7]
array = mergesort(array)
print array
