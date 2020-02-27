## Knapsack with repetition using dynamic programming ##

## Problem: You can only carry a certain weight, you want to maximize the value of item s




## INPUT: W -- total weight that you can carry
##        w_1,w_2,..,w_n -- weight of each item
##        v_1,v_2,..,v_n -- value of each item
## OUTPUT: Max value without exceeding total weight, W where we can take as many as each item as we want.



def k(W, weights, values):
    n = len(weights)
    table = [0 for x in range(W + 1)]
    
    for i in range(1, W + 1):
        j = 0
        curr_max = 0
        while (j < n and weights[j] <= i):
            if i - weights[j] >= 0 and curr_max < table[i - weights[j]] + values[j]:
                curr_max = table[i - weights[j]] + values[j]
            j += 1
        table[i] = curr_max

    return table[W]


print("k(10, [6, 3, 4, 2], [30, 14, 16, 9]) =", k(10, [6, 3, 4, 2], [30, 14, 16, 9]))
print("It should be 48 (one of item 1 and two of item 4).")
        

    
