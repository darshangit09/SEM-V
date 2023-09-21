def lcs(X, Y):
    m = len(X)
    n = len(Y)
  
    L = [[0] * (n + 1) for i in range(m + 1)]
  
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
  
    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # # Print the table
    print("Table:")
    for row in L:
        print(row)

    return lcs

X = "ACCGGTCGAGTG"
Y = "GTCGTTCGGAAT"
Z = lcs(X, Y)
print("String 1: " + X)
print("String 2: " + Y)
print("LCS: " + Z )
print("Length of LCS is : "+str(len( Z )))
