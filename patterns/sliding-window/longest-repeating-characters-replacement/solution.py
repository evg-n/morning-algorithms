from collections import defaultdict

def longest_repeating_character_replacement(s, k):
    max_freq, freq, max_window_len = 0, defaultdict(int), 0

    l, i = 0, 0
    while i < len(s):
        freq[s[i]] += 1
        max_freq = max(max_freq, freq[s[i]])
        cur_window_len = (i - l + 1) 
        if cur_window_len > max_freq + k:
            freq[s[l]] -= 1
            l += 1
        else:
            max_window_len = max(max_window_len, cur_window_len)
        
        i += 1
    
    return max_window_len


if __name__ == "__main__":
    assert longest_repeating_character_replacement("AABCCBB", 2) == 5
    assert longest_repeating_character_replacement("AAACBBBAABAB", 2) == 6
    assert longest_repeating_character_replacement("BBBAABAB", 2) == 6
