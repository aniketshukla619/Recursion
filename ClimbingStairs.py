# https://leetcode.com/problems/climbing-stairs/description/
# Not an optimized solution

def climbStairs(num: int) -> int:
    """
    Climbing Stairs Problem.
    Args:
        num (int) : num steps to reach the top.
    Returns:
        int : distinct ways to reach the top
    """
    if num <= 1:
        return 1
    return climbStairs(num-1) + climbStairs(num-2)


## Optimized Solution - With memoization

def climbStairs_memoized(num: int, cache: dict = {}) -> int:
    """
     Climbing Stairs Problem.
    Args:
        num (int) : num steps to reach the top.
    Returns:
        int : distinct ways to reach the top
    """
    if num <= 1:
        return 1
    if num in cache:
        return cache[num]
    cache[num] = climbStairs_memoized(num-1) + climbStairs_memoized(num-2)
    return cache[num]
