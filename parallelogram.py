n = 4 
for row in range (2 * n - 1):
    for col in range (n):
        if row + col == n - 1 or row + col == 2 * n - 1 or col == 0 and row >= n - 1 or col == n - 1 and row <= n - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
