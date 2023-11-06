# Move Zeros'a Daha profesyönel bir yaklaşım:

nums = [1,3,5,17,0,0]

prev_idx = 0
for i in range(0, len(nums)):
    if nums[i] != 0:
        hold = nums[prev_idx]
        nums[i] = hold
        prev_idx += 1

print(nums)