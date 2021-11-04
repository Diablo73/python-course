def transposeMatrix(mat):
	a = [[] for i in range(len(mat[0]))]
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			a[j].append(mat[i][j])
	return a


def printMatrix(mat):
	for i in mat:
		print(*i)


if __name__ == '__main__':
	matrix = [[1, 2, 3], [4, 5, 6]]
	ans = transposeMatrix(matrix)

	print("Original Matrix =")
	printMatrix(matrix)
	print("Transposed Matrix =")
	printMatrix(ans)
