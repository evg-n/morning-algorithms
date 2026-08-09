# Linked list cycle IV

**Patterns:** 
- fast & slow pointers

**First solved:** Date: 2026-06-12

## Problem (in my own words)
Given the head of a singly linked list, implement a function to detect and remove any cycle present in the list. Modify the linked list in place, ensuring it remains acyclic while preserving the original node order. If no cycle is found, return the linked list as is.

## Intuition
- Using floyd's algorithm to find cycle entrance and keep tracking prev node. This will be the last node after we drop the cycle.

## What I missed / mistakes

## Complexity
O(n) time, O(1) space.

## Re-solve log

