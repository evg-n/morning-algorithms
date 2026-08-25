def diet_plan_performance(calories, k, lower, upper):
    performance = 0
    window_sum = sum(calories[:k])
    
    if window_sum < lower:
        performance -= 1
    elif window_sum > upper:
        performance += 1
    
    for i, num in enumerate(calories[k:], start=k):
        window_sum += calories[i]
        window_sum -= calories[i - k]
        if window_sum < lower:
            performance -= 1
        elif window_sum > upper:
            performance += 1

    return performance
