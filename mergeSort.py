def merge(A, start, end):
	L = A[start:(start + end)/2+1]
	R = A[(start + end)/2 + 1:( end+1)]
	L.append(10**9)
	R.append(10**9)
	i = 0
	j = 0
	for k in range(start, end + 1):
		if L[i] > R[j]:
			A[k] = R[j]
			j = j + 1
		elif L[i] < R[j]:
			A[k] = L[i]
			i = i + 1

def mergeSort(A, start, end):
	if len(A[start:(end+1)]) == 1:
		return A[start:(end+1)]
	elif len(A[start:(end+1)]) == 2:
		if A[start] > A[end]:
			A[start], A[end] = A[end], A[start]
		return A[start:(end+1)]
	else:
		mergeSort(A, start, (start+end)/2)
		mergeSort(A, (start+end)/2 + 1, end)
		merge(A,start, end)

A = [9,8,7,6,5,4,3,2,1,0,-1,-2,-2,-3]
print "Before MergeSort: ", A
mergeSort(A, 0, len(A)-1)
print "After MergeSort: ", A