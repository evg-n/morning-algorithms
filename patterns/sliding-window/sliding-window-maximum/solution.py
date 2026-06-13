def find_max_sliding_window(nums, w):
    if w == 1:
        return nums
    
    
    curr_max = max(nums[:w])
    results = [curr_max]

    for i in range(w, len(nums)):
        l = i - w
        if nums[l] == curr_max:
            curr_max = max(nums[l + 1:i + 1])
        else:
            curr_max = max(curr_max, nums[i])
        results.append(curr_max)
    
    return results



if __name__ == "__main__":
    assert find_max_sliding_window([-4, 2, -5, 3, 6], 3) == [2, 3, 6]
    assert find_max_sliding_window([-4, 5, 4, -4, 4, 6, 7, 20], 2) == [5, 5, 4, 4, 6, 7, 20]
