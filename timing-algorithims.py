#Hypothesis:
'''
I hypothesize that Merge sort will start to become more efficient that insertion sort as n becomes bigger than 1,000. 
My intuition says that insertion sort will be more efficient for values lesser than 1,000, perhaps only less than 100.
I have this intuition paritally based on prior knowledge as I know for small collections, insertion sort is prefered over merge sort, I just am not sure exactly how small.
'''
#Conclusion
'''
My main conclusion of the experiment is that insertion sort is clearly superior than merge sort when n is between the ranges of 10-50. 
Between the ranges of 50-70 things become indistinguishable. 
Between the range of 70-80 merge sort starts to emerge as the better algorithm, and continues to do so, until it is very obvious for values of n = 100 and greater. 
'''

#Source:
'''
Merge sort source: https://www.geeksforgeeks.org/python-program-for-merge-sort/
Insertion sort course: https://www.geeksforgeeks.org/insertion-sort/
'''

import timeit
import random
# Python program for implementation of MergeSort
# This code is contributed by Mohit Kumra
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0   # Initial index of first subarray
    j = 0   # Initial index of second subarray
    k = l   # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        
#Insertion sort pseduo 
# This code is contributed by Mohit Kumra
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

#Helper function used by my test methods 
def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]
#Test method for insertion
def test_insertion_sort(size):
    arr = generate_random_array(size)
    insertionSort(arr)
#Test method for merge   
def test_merge_sort(size):
    arr = generate_random_array(size)
    mergeSort(arr, 0, len(arr) - 1)
    
#Can edit these for various tests.. create different ranges.. etc.
array_sizes = [10, 100, 1000, 10000, 100000, 1000000]

#N = 10
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[0]), number=1)
print(f"Merge sort: Execution time for array of size {array_sizes[0]}: {execution_time:.5f} seconds")
execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[0]), number=1)
print(f"Insertion sort: Execution time for array of size {array_sizes[0]}: {execution_time:.5f} seconds")

#N = 100
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[1]), number=1)
print(f"Merge sort: Execution time for array of size {array_sizes[1]}: {execution_time:.5f} seconds")
execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[1]), number=1)
print(f"Insertion sort: Execution time for array of size {array_sizes[1]}: {execution_time:.5f} seconds")

#N = 1000
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[2]), number=1)
print(f"Merge sort: Execution time for array of size {array_sizes[2]}: {execution_time:.5f} seconds")
execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[2]), number=1)
print(f"Insertion sort: Execution time for array of size {array_sizes[2]}: {execution_time:.5f} seconds")


#N = 10000
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[3]), number=1)
print(f"Merge sort: Execution time for array of size {array_sizes[3]}: {execution_time:.5f} seconds")
execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[3]), number=1)
print(f"Insertion sort: Execution time for array of size {array_sizes[3]}: {execution_time:.5f} seconds")

# N = 100000
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[4]), number=1)
print(f"Merge sort: Execution time for array of size {array_sizes[4]}: {execution_time:.5f} seconds")
#Insertion sort takes way to long to run.. so I comment it out:
# execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[4]), number=1)
# print(f"Execution time for array of size {array_sizes[4]}: {execution_time:.5f} seconds")

#N = 1000000 
N = 1000000
execution_time = timeit.timeit(lambda: test_merge_sort(array_sizes[5]), number=1)
#Insertion sort takes way to long to run.. so I comment it out:
# print(f"Merge sort: Execution time for array of size {array_sizes[5]}: {execution_time:.5f} seconds")
# execution_time = timeit.timeit(lambda: test_insertion_sort(array_sizes[5]), number=1)
# print(f"Execution time for array of size {array_sizes[5]}: {execution_time:.5f} seconds")


#Alertnate testing method for various sizes.. could potentailly impact time values due to spinning up for loop... to be tested..
# for size in array_sizes:
#     execution_time = timeit.timeit(lambda: test_merge_sort(size), number=1)
#     print(f"Execution time for array of size {size}: {execution_time:.5f} seconds")
