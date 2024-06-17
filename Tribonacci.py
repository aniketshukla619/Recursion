# https://leetcode.com/problems/n-th-tribonacci-number/
# Not an optimized solution

def tribonacci(num: int) -> int:
    """
    Returns Tribonacci number
    Args:
        num (int): num to print tribonacci sequence
    Returns:
        int: Returns tribonacci sequence
    """
    if num == 0:
        return num
    if num <= 2:
        return 1
    return tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)

## Optimized Solution - With memoization

def tribonacci_memoized(num: int, cache: dict = {}) -> int:
    """
    Returns Tribonacci number
    Args:
        num (int): num to print tribonacci sequence
    Returns:
        int: Returns tribonacci sequence
    """
    if num == 0:
        return num
    if num <= 2:
        return 1
    if num in cache:
        return cache[num]
    cache[num] = tribonacci_memoized(num-1) + tribonacci_memoized(num-2) \
                + tribonacci_memoized(num-3)
    return cache[num]
