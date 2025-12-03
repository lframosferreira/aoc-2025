from sys import stdin
ans=0
for line in stdin:
    nums = [int(c) for c in line if c != '\n']
    mx=max(nums)
    idx=nums.index(mx)
    if idx == len(nums)-1:
        ans += max(nums[:idx])*10 + mx
        pass
    else:
        ans+= mx*10 + max(nums[idx+1:])

print(ans)

