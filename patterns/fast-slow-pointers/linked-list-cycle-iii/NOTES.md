# Linked list cycle III

**Patterns:** 
- fast & slow pointers

**First solved:** Date: 2026-06-12

## Problem (in my own words)
Given the head of a linked list, determine the length of the cycle present in the linked list. If there is no cycle, return 0.

## Intuition
- Using floyd's algorithm to find cycle entrance (fast fail if no exit). Count the cycle length by tracersing the whole loop.

## What I missed / mistakes

## Complexity
O(n) time, O(1) space.

## Re-solve log

