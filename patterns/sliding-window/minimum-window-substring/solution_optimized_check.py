from collections import defaultdict

def min_window(s, t):
    t_freq = defaultdict(int)
    for ch in t:
        t_freq[ch] += 1
    cur_len, req_len = 0, len(t_freq)

    min_window, w_freq = "", defaultdict(int)
    l = r = 0
    while r < len(s):
        ch = s[r]
        if ch in t_freq:
            w_freq[ch] += 1
            if w_freq[ch] == t_freq[ch]:
                cur_len += 1
            
        while cur_len == req_len:
            if min_window == "" or (r - l + 1) < len(min_window):
                min_window = s[l:r + 1]
            
            lch = s[l]
            if lch in t_freq:
                w_freq[lch] -= 1
                if w_freq[lch] < t_freq[lch]:
                    cur_len -= 1
            l += 1
        r += 1

    return min_window


if __name__ == "__main__":
    assert min_window("abaacbba", "abc") == "acb"
    assert min_window("abaacbab", "abcc") == ""
    assert min_window("acbbaca", "aba") == "baca"
