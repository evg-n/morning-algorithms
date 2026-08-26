from collections import defaultdict

def contains_nearby_duplicate(nums, k):
    if k < 1:
        return False
    
    window = defaultdict(int)
    for i, num in enumerate(nums[:k]):
        if num in window:
            return True
        window[num] = i
    
    for i, num in enumerate(nums[k:], start=k):
        l = i - k
        if num in window and window[num] >= l:
            return True
        
        window[num] = i
    
    return False
