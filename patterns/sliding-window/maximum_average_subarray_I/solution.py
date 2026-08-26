def find_max_average(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    
    for i, num in enumerate(nums[k:], start=k):
        window_sum -= nums[i - k]
        window_sum += num
        max_avg = max(max_avg, window_sum / k)
    
    return max_avg
