#Given an array nums of n integers where n > 1, return an array output
#such that output[i] is equal to the product of all the elements of
#nums except nums[i].


def product_expect_self(nums):
    n = len(nums)

    L, R, result = [0] * n, [0] * n, [0] * n

    for i in range(n):
        if i == 0:
            L[i] = 1
        else:
            L[i] = L[i-1] * nums[i - 1]



    for i in range(n-1, -1, -1):
        if i == n-1:
            R[i] = 1
        else:
            R[i] = R[i+1] * nums[i+1]


    for i in range(n):
        result[i] = L[i] * R[i]

    return result



a = [1, 2, 3, 4]

print(str(product_expect_self(a)) + " <------------- Should be [24, 12, 8, 6]")
