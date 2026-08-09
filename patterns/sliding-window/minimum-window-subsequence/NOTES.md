# Minimum window subsequence
LeetCode 727 - https://leetcode.com/problems/minimum-window-subsequence/

**Patterns:** 
- sliding window

**First solved:** Date: 2026-08-08

## Problem (in my own words)
Given two strings, s1 and s2, find and return the shortest substring of s1 in which all the characters of s2 appear in the same order, but not necessarily next to each other (i.e., s2 should be a subsequence of the substring).

## Intuition
- Sliding window optimized on repeated scanning, backwards shrinking to skip redundant forward searches

## What I missed / mistakes
Long thinking about solution after a month+ pause of practice. And coming up with O(N * N) solution only.


## Complexity
O(n * m) time, O(1) space.

## Re-solve log
- [ ] 2026-09-11 (+1 month)
