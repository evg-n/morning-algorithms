# Palindrome linked list
LeetCode 234 - https://leetcode.com/problems/palindrome-linked-list/

**Patterns:** 
- fast & slow pointers

**First solved:** Date: 2026-06-11


## Problem (in my own words)
Given the head of a linked list, your task is to check whether the linked list is a palindrome or not. Do not modify the structure of the linked list before and after the checking process.

## Intuition
Treat the array as a linked list: index -> value is a "next pointer".
A duplicate value means two indices point to the same node → a cycle.
Cycle entrance = the duplicate. Floyd's algorithm finds it in O(1) space.

## What I missed / mistakes
- I've missed the easies solution that involves changing the underlying structure of the linked list, but I've managed to complete the recursion trick to bypass this restriction which is intself is nice.

## Complexity
O(n) time, O(1) space.

## Re-solve log
- [ ] 2026-07-11 (+1 month)
