# Two Sum Solution
# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
