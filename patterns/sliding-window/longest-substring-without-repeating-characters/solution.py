from collections import defaultdict

def find_longest_substring(input_str):
   longest_len, l = 0, 0
   cache_idx = {}
   
   for i, ch in enumerate(input_str):
      if ch in cache_idx and cache_idx[ch] >= l:
         longest_len = max(longest_len, i - l)
         l = cache_idx[ch] + 1 
      
      cache_idx[ch] = i
   
   return max(longest_len, len(input_str) - l)
   