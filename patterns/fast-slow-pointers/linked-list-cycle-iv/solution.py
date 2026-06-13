def remove_cycle(head):
    if not head or not head.next:
        return head
    
    slow, fast, prev = head.next, head.next.next, None
    while slow != fast and fast and fast.next:
        slow = slow.next
        prev, fast = fast.next, fast.next.next

    if not fast or not fast.next:
        return head
    
    slow = head
    while slow != fast:
        slow = slow.next
        prev, fast = fast, fast.next

    prev.next = None
    return head


if __name__ == "__main__":
    from helpers.linked_list import build_cycle, to_list
    l1 = build_cycle([3,6,9,10,11], 0)
    print(to_list(remove_cycle(l1)))
