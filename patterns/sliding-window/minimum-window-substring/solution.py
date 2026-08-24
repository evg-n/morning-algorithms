from collections import defaultdict

def is_window_contains_t(w_freq, t_freq):
    for k, v in t_freq.items():
        if k not in w_freq or w_freq[k] < t_freq[k]:
            return False
    return True

def min_window(s, t):
    t_freq = defaultdict(int)
    for ch in t:
        t_freq[ch] += 1

    min_window, w_freq = "", defaultdict(int)
    l = r = 0
    while r < len(s):

        if min_window != "":
            w_freq[s[l]] -= 1
            l += 1
        w_freq[s[r]] += 1
        while is_window_contains_t(w_freq, t_freq):
            if min_window == "" or (r - l + 1) < len(min_window):
                min_window = s[l:r + 1]
                print('new min window: ', s[l: r +1], l, r)
            w_freq[s[l]] -= 1
            l += 1
        r += 1

    return min_window


if __name__ == "__main__":
    assert min_window("abaacbba", "abc") == "acb"
    assert min_window("abaacbab", "abcc") == ""
    assert min_window("acbbaca", "aba") == "baca"
