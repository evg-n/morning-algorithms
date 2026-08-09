def get_subsequence_end_idx(start_idx, s1, s2, max_window_length):
    i, k = start_idx, 0
    while i < min(start_idx + max_window_length, len(s1)) and k < len(s2):
        if s1[i] == s2[k]:
            k += 1
        i += 1

    if k == len(s2):
        return i - 1
    return -1

def minWindow(s1, s2):
    l, r = 0, len(s1)


    for i, ch in enumerate(s1):
        if ch == s2[0]:

            max_window_length = len(s1) if r == len(s1) else r - l
            idx = get_subsequence_end_idx(i, s1, s2, max_window_length)
            
            if idx != -1:
                l, r = i, idx

    if r == len(s1):
        return ""
    
    return s1[l : r + 1]

if __name__ == "__main__":
    assert minWindow("abcdebdde", "bde") == "bcde"
    assert minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "kzed")
