import sys


def maxNum(nums: list[int]):
    n = len(nums)
    max_val = -sys.maxsize - 1
    max_index = 0
    for i in range(n):
        if nums[i] > max_val:
            max_val = nums[i]
            max_index = i
    return max_val, max_index
