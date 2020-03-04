## Given an array of integers and a target integer output the two indices that add to the target

def two_sum(nums, target):
    d ={}

    for i in range(len(nums)):
        complement = target - nums[i]
        if (complement in d.keys()):
            return (d[complement], i)
        else:
            d[nums[i]] = i

    print("No pair adds up to " + str(target))



print(two_sum([11, 5, 2, 7], 9)) # should return 2 3
