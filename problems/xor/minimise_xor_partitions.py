"""
You are given an integer array nums and an integer k.

Your task is to partition nums into k non-empty.

For each subarray, compute the bitwise XOR of all its elements.

Return the minimum possible value of the maximum XOR among these k subarrays.

Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
"""

def solve(nums: list[int], k: int) -> int:
    # Step 1: Prefix XOR
    n = len(nums)
    pfix = [0] * (n + 1)
    for i in range(1, n + 1):
        pfix[i] = pfix[i - 1] ^ nums[i - 1]

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][1] = pfix[i]  # Base case: 1 partition
    
    for parts in range(2, k + 1):
        for end in range(parts, n + 1):
            for split in range(parts - 1, end):
                # fast xor
                segment = pfix[end] ^ pfix[split]
                # min max
                maxXor = max(dp[split][parts - 1], segment)
                dp[end][parts] = min(dp[end][parts], maxXor)
                
    return dp[n][k]


print(solve([1,1,2,3,1], 2))




    
