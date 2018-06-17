A=[12,3,43,2,34,54,67]
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
		print("in loop->",A)
			
	return A
print(insertion_sort1(A))
