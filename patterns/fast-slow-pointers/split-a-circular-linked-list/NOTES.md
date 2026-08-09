# Split a circular linked list
LeetCode 2674 - https://leetcode.com/problems/split-a-circular-linked-list/

**Patterns:** 
- fast & slow pointers

**First solved:** Date: 2026-06-12

## Problem (in my own words)
Given a circular linked list, list, of positive integers, split it into two circular linked lists. The first circular linked list should contain the first half of the nodes (exactly ⌈list.length / 2⌉ nodes) in the same order they appeared in the original list, while the second circular linked list should include the remaining nodes in the same order.

## Intuition
Again, we need to split the list in half, so find mid via fast & slow technique is the core intuition.

## What I missed / mistakes
- First, I've put the wrong condition to stop when finding middle. Not until None but until head is met.

## Complexity
O(n) time, O(1) space.

## Re-solve log

