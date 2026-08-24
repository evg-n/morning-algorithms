def min_sub_array_len(target, nums):
    result, window_sum = float('Inf'), 0
    
    l, r = 0, 0
    while r < len(nums):
        
        window_sum += nums[r]
        if result != float('Inf'):
            window_sum -= nums[l]
            l += 1
        while window_sum >= target:
            result = min(result, r - l + 1)
            window_sum -= nums[l]
            l += 1
        
        r += 1
    
    return 0 if result == float('Inf') else result
