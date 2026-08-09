from collections import deque

def insert(idx: int, nums: list[int], window: deque):
    while window and nums[window[-1]] <= nums[idx]:
        window.pop()
    window.append(idx)

def find_max_sliding_window(nums, w):
    if w == 1:
        return nums
    
    window = deque()
    for i, _ in enumerate(nums[:w]):
        insert(i, nums, window)
    
    results = [nums[window[0]]]

    for i, _ in enumerate(nums[w:], start=w):
        if window[0] <= i - w:
            window.popleft()
        
        insert(i, nums, window)
        results.append(nums[window[0]])
    
    return results


if __name__ == "__main__":
    assert find_max_sliding_window([-4, 2, -5, 3, 6], 3) == [2, 3, 6]
    assert find_max_sliding_window([-4, 5, 4, -4, 4, 6, 7, 20], 2) == [5, 5, 4, 4, 6, 7, 20]
