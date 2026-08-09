# Sliding window maximum
LeetCode 239 - https://leetcode.com/problems/sliding-window-maximum/

**Patterns:** 
- sliding window

**First solved:** Date: 2026-08-01

## Problem (in my own words)
You are given an array of integers nums and a sliding window of size w that moves from left to right across the array, shifting one position at a time.

Your task is to find the maximum value within the current window at each step and return it.

## Intuition
- Use deque to keep O(n) time

## What I missed / mistakes
I've missed the deque approach. Implemented O(n * w) solution with possible wasting current window maximum search on each step

## Complexity
O(n) time, O(w) space.

## Re-solve log
