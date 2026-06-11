def get_cycle_start_idx(i, nums):
    start_idx = nums[i]
    slow, fast = nums[start_idx], nums[nums[start_idx]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    fast = nums[i]
    
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
    return slow


def find_duplicate(nums):
    idx = get_cycle_start_idx(0, nums)
    return idx
