# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def contains_dup(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen.keys():
            return True
        else:
            seen[nums[i]] = i
    return False


a = [1, 2, 3, 1]

print(str(contains_dup(a)) + " should be true")

a = [1, 2, 3, 4]

print(str(contains_dup(a)) + " should be false")
