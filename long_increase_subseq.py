# Input: unsorted array of ints 
# Output: lenght of longest increasing substring


# Example:
## [10, 9, 2, 5, 3, 7, 101, 18] --> 4
## because the longest increasing subsequence is
## [2, 3, 7, 101] which is of length 4



def LIS(nums):
    
    n = len(nums)

    if n == 0:
        return 0
    
    table = [1 for x in range(n)]
    max_seen = 1
    
    for i in range(n):
        if i == 0:
            table[i] = 1
        else:
            for j in range(0, i):
                if nums[j] < nums[i] and table[j] >= table[i]:
                    table[i] = 1 + table[j]
        if table[i] > max_seen:
            max_seen = table[i]

    return max_seen


if __name__ == '__main__':
    print(LIS([10, 9, 2, 5, 3, 7, 101, 18]))
