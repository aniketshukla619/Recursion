# https://leetcode.com/problems/fibonacci-number
# Not an optimized solution

def fib(num: int) -> int:
    """
    Prints Fibonacci series
    Args:
        num (int): num to print fibonacci sequence
    Returns:
        int: Returns fibonacci sequence
    """
    if num <= 1:
        return num
    return fib(num-1) + fib(num-2)
