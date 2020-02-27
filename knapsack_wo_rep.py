## Knapsack without reptitions using dynamic programming ##

## Similar idea as previous knapsack but you cannot take multiple of
## the same item



## INPUT and OUTPUT is the same as previous problems (See knapsack_w_rep.py) ##



def k(W, weights, values):
    n = len(weights)

    table = [[0 for x in range(n + 1)] for x in range(W + 1)]

    for j in range(n + 1):
        for w in range(W + 1):
            if j == 0:
                table[w][j] = 0
            elif w == 0:
                table[w][j] = 0
            elif weights[j - 1] > w:
                table[w][j] = table[w][j - 1]
            else:
                table[w][j] = max(table[w][j - 1], table[w - weights[j - 1]][j - 1] + values[j - 1])

    return table[W][n]



print("k(10, [6, 3, 4, 2], [30, 14, 16, 9]) =", k(10, [6, 3, 4, 2], [30, 14, 16, 9]))
print("It should be 46 (one of item 1 and item 2).")

