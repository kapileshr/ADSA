def matrix_chain_mult(dimensions):
    num_matrices = len(dimensions) - 1
    dp = [[float('inf')] * num_matrices for _ in range(num_matrices)]


    for i in range(num_matrices):
        dp[i][i] = 0


    for chain_length in range(2, num_matrices + 1):
        for i in range(num_matrices - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):

                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][num_matrices - 1]



matrices = [(2, 3), (3, 4), (4, 2)]
min_scalar_mult = matrix_chain_mult(matrices)
print("Minimum Scalar Multiplications:", min_scalar_mult)
