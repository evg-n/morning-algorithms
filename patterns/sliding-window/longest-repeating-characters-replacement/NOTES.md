# Longest repeating characters replacement
LeetCode 424 - https://leetcode.com/problems/longest-repeating-character-replacement/

**Patterns:** 
- sliding window

**First solved:** Date: 2026-08-12

## Problem (in my own words)
Given a string, s, and an integer, k, find the length of the longest substring in s, where all characters are identical, after replacing, at most, k characters with any other uppercase English character.

## Intuition
- Keep freq map. Don't need to check the current max freq every time, just update it if larger with the right most element in current window.

## What I missed / mistakes
Don't come up with any solution. Asked for 2-3 hints from gpt.


## Complexity
O(n) time, O(1) space.

## Re-solve log
- [ ] 2026-09-12 (+1 month)
