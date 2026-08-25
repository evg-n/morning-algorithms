# Minimum window substring
LeetCode 76 - https://leetcode.com/problems/minimum-window-substring/

**Patterns:** 
- sliding window

**First solved:** Date: 2026-08-23

## Problem (in my own words)
Statement
Given two strings, s and t, find the minimum window substring in s, which has the following properties:

It is the shortest substring of s that includes all of the characters present in t.
It must contain at least the same frequency of each character as in t.
The order of the characters does not matter here.


## Intuition
- Sliding window, store frequences. Clever optimizations are:
1) Don't store freq characters that are not in target t
2) If a given frequency matches what we expect in t, just add one. Until you meet target_len

## What I missed / mistakes
Long thinking. And I missed these two optimizations, implementing O(M * N) with costly checks first, then optimized version after lookup.


## Complexity
O(n + m) time, O(1) space.

## Re-solve log
- [ ] 2026-09-25 (+1 month)
