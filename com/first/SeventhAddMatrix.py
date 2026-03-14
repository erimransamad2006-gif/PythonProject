# Define two 3x3 matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Create a matrix to store the sum
sum_matrix = []

# Perform addition
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    sum_matrix.append(row)

# Display result
print("Sum of the two matrices:")
for row in sum_matrix:
    print(row)



# multiply
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Create a result matrix filled with 0
result = [[0 for j in range(len(B[0]))] for i in range(len(A))]

# Matrix multiplication logic
for i in range(len(A)):          # loop over rows of A
    for j in range(len(B[0])):   # loop over columns of B
        for k in range(len(B)):  # loop over columns of A / rows of B
            result[i][j] += A[i][k] * B[k][j]

# Display the result
print("Multiplication / Resultant Matrix (A × B):")
for row in result:
    print(row)
