# Find the Duplicate Number
LeetCode 287 - https://leetcode.com/problems/find-the-duplicate-number/

**Patterns:** 
- fast & slow pointers

**Difficulty:** Medium

**First solved:** Date: 2026-06-11


## Problem (in my own words)
Array of n+1 integers, each in [1..n], exactly one value repeated
(possibly many times). Find it. Constraints: no modifying the array,
O(1) extra space.

## Intuition
Treat the array as a linked list: index -> value is a "next pointer".
A duplicate value means two indices point to the same node → a cycle.
Cycle entrance = the duplicate. Floyd's algorithm finds it in O(1) space.

## What I missed / mistakes
- Tried to derive some other solutions, ignored Floyd's algorithm and then spent too much time remembering the "why" it works.

## Complexity
O(n) time, O(1) space.

## Re-solve log
- [ ] 2026-07-11 (+1 month)
