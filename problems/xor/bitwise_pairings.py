"""
You are given two arrays, nums1 and nums2, consisting of non-negative integers.
Let there be another array, nums3, which contains the bitwise XOR of all pairings of
integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.
"""

from itertools import product
def solve(nums1: list[int], nums2: list[int]) -> int:
    # O(n^2)
    nums3 = [
        a ^ b for a,b in list(product(nums1, nums2))
    ]
    ans = 0
    for n in nums3:
        ans ^= n
        
    return ans

def solve2(nums1: list[int], nums2: list[int]) -> int:
    l1, l2 = len(nums1), len(nums2)
    ans = 0
    
    if l2 % 2:
        for n in nums1:
            ans ^= n
            
    if l1 % 2:
        for n in nums2:
            ans ^= n            
    return ans






