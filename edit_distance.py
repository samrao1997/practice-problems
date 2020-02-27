### Edit Distance with dynamic programming

## INPUT: two strings: wrd1, wrd2
## OUTPUT: minimum number of operation to change wrd1 into wrd2

## operations: insetions, deletions , and substitutions of characters


## EXAMPLE:
## wrd1 = SNOWY, wrd2 = SUNNY
## _ S N O W _ Y
## S U N _ _ N Y
## This is the best possible alignment so our function would return 3



def ED(wrd1, wrd2):
    m = len(wrd1)
    n = len(wrd2)

    table = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # the entry of table[i][j] represents the edit distance from word1[:i] to word2[:j]
    #  so for table[0][j] would be edit distance for "" to word[:
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif wrd1[i -1] == wrd2[j - 1]:
                table[i][j] = table[i - 1][j -1]
            else:
                table[i][j] = 1 + min(table[i - 1][j],
                                      table[i][j - 1],
                                      table[i - 1][j -1])

    return table[m][n]




print(ED("SNOWY", "SUNNY"), ": it should be 3")
            
                
