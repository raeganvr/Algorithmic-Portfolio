# Climbing Stairs

## Problem Description
Given `n` steps, each time you can either climb 1 or 2 steps. Determine the number of distinct ways to reach the top of a staircase with `n` steps.

## Intuition
The problem a pattern similar to the Fibonacci sequence. To reach the `n`th step, you can:
1. Take a single step from the (n-1)th step.
2. Take two steps from the (n-2)th step.

Thus, the number of ways to reach the `n`th step, `ways(n)`, can be expressed as:
   $$ways(n) = ways(n - 1) + ways(n - 2)$$

## Approach
I used a dynamic programming approach with a single-pass loop. We initialize two base cases: the number of ways to climb 0 steps (1 way, by doing nothing) and the number of ways to climb 1 step (also 1 way). For each step from 2 up to `n`, we compute the ways to reach that step by summing the ways to reach the two previous steps. This allows us to calculate the result in `O(n)` time without using extra space for an array.

## Complexity
- **Time Complexity**: $$O(n)$$  
   We iterate from 2 up to `n`, making it an `O(n)` solution.

- **Space Complexity**: $$O(1)$$  
   Only two variables are used to store the previous results, so the space complexity is constant.

## Solution Code
```python3 []
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Cases
        if n <= 1:
            return 1
        one_step_back = 1  # ways to climb to step 1
        two_steps_back = 1  # ways to climb to step 0
        
        # Calculate ways to reach each step up to n
        for step in range(2, n + 1):
            current = one_step_back + two_steps_back
            # Update steps 
            two_steps_back = one_step_back
            one_step_back = current
        
        return one_step_back

```
## Example
- Input: n = 5
- Output: 8
- Explanation: There are 8 distinct ways to reach the 5th step, following a sequence similar to the Fibonacci series.
