# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

## Intuition
Initially, I considered a brute-force solution that would compare each element to every subsequent element, resulting in an $$O(n^2)$$ runtime. By focusing on optimization, I realized that using a hash map could reduce the runtime to $$O(n)$$ by enabling constant-time operations for search, storage, and retrieval.

## Approach
I implemented a single-pass solution using a hash map to store each number’s index as we iterate. For each number, I calculate its complement (the value needed to reach the target). If this complement is already in the hash map, we’ve found our pair, and the indices are returned. If the complement isn’t found, I add the current number and its index to the hash map to check against future elements.

## Complexity
- **Time Complexity**: $$O(n)$$  
   We pass through the list once, with $$O(1)$$ hash map operations per element, resulting in an overall $$O(n)$$ time complexity.

- **Space Complexity**: $$O(n)$$  
   In the worst case, the hash map could store all $$n$$ elements if no solution is found until the end of the list.

## Solution Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i in range (0,len(nums)):
            complement = target - nums[i]
            if complement in num_index:  
                return [i, num_index[complement]]
            num_index[nums[i]] = i 
         
```
## Example
- Input: nums = [2, 7, 11, 15], target = 9
- Output: [0, 1]





