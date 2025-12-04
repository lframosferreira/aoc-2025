from sys import stdin
for line in stdin:
    nums = [int(c) for c in line if c != '\n']
    dp = [-1 for _ in range(13)]
    for idx, num in enumerate(nums):
        for i in range(13):
            if dp[i]==-1:
                dp[i]=dp[i-1]*10+num
            else:
                dp[i]=max(dp[i-1]*10+num, dp[i])
print(dp)

