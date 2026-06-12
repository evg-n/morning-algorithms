# Maximum twin sum of a linked list
LeetCode 2130 -https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

**Patterns:** 
- fast & slow pointers

**Difficulty:** medium

**First solved:** Date: 2026-06-12


## Problem (in my own words)
Given the head of a linked list with an even number of nodes, return the maximum twin sum among all pairs.

## Intuition
The intuition is to traverse the linked list from both ends. And task constraints allow list ds modification. So, use fast and slow pointers to determine the middle point of the list, reverse the rest and compare one by one sums.

## What I missed / mistakes
- Prev task used the find middle algorithm in linked list, so I was comfortable here with fresh memory of solution.

## Complexity
O(n) time, O(1) space.

## Re-solve log

