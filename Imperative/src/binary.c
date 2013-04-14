#include <stdio.h>
#include <binary.h>
int
binarysearch(int arr[], int value, size_t low, size_t high)
{
	if(low >= high)
		return -1;
	int middle = (low+high)/2;
	if(arr[middle] == value)
	{
		return middle;
	}
	else if(arr[middle] > value)
	{
		return binarysearch(arr, value, low, middle);
	}
	else if(arr[middle] < value)
	{
		return binarysearch(arr, value, middle+1, high);
	}
	return -1;

}
int
BinarySearch(int arr[], int value, size_t size)
{
	return binarysearch(arr, value, 0, size);

}

