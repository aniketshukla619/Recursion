# https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Not an optimized solution

# library imports
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    """
    Climbing Stairs Problem with cost.
    Args:
        cost (List) : cost where cost[i] is the cost of ith step on a staircase
    Returns:
        int : minimum cost to reach top of the floor
    """
    # Adding zero cost to handle overflow condition
    cost.append(0)

    def helper(cost: List[int], idx: int) -> int:
        """
        helper function to perform recursion.
        """
        if idx < 0:
            return 0
        return cost[idx] + \
            min(helper(cost, idx-1), helper(cost, idx-2))
    return helper(cost, len(cost)-1)


# Optimized Solution - With memoization

def minCostClimbingStairs_memoized(cost: List[int]) -> int:
    """
     Climbing Stairs Problem with cost.
    Args:
        cost (List) : cost where cost[i] is the cost of ith step on a staircase
    Returns:
        int : minimum cost to reach top of the floor
    """
    # Adding zero cost to handle overflow condition
    cost.append(0)

    def helper(cost: List[int], idx: int, cache: dict) -> int:
        """
        helper function to perform recursion.
        """
        if idx < 0:
            return 0
        if idx in cache:
            return cache[idx]
        cache[idx] = cost[idx] + \
            min(helper(cost, idx-1, cache), helper(cost, idx-2, cache))
        return cache[idx]
    return helper(cost, len(cost)-1, cache={})
