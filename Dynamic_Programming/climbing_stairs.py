# Climbing Stairs Solution
# Given n steps, where each step can be climbed either 1 or 2 steps at a time,
# return the number of distinct ways to climb to the top.

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
