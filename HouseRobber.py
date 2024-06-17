# https://leetcode.com/problems/house-robber/
# Not an optimized solution

from typing import List

def houseRob(nums: List[int]) -> int:
    """
    House Robbing problem.
    Args:
        nums (List) : Amount of money each house has.
    Returns:
        int : Max amount of money you can rob.
    """
    def helper(idx: int, nums: List[int]):
        if idx < 0:
            return 0
        return max(nums[idx] + helper(idx-2, nums),
                   helper(idx-1, nums))

    return helper(len(nums)-1, nums)


# Optimized Solution - With memoization

def houseRob_memoized(nums: List[int]) -> int:
    """
    House Robbing problem with memoization.
    Args:
        nums (List) : Amount of money each house has.
    Returns:
        int : Max amount of money you can rob.
    """
    def helper(idx: int, nums: List[int], cache: dict):
        if idx < 0:
            return 0
        if idx in cache:
            return cache[idx]
        rob = nums[idx] + helper(idx-2, nums, cache)
        notRob = helper(idx-1, nums, cache)
        cache[idx] = max(rob, notRob)
        return cache[idx]

    return helper(len(nums)-1, nums, cache={})
