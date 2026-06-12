def reverse_list(node):
    prev, curr, next = None, node, node.next
    while True:
        curr.next = prev
        if not next:
            break
        prev, curr, next = curr, next, next.next
    return curr


def twin_sum(head):
    slow, fast = head, head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    last = reverse_list(slow.next)
    first = head
    
    max_sum = 0
    while last:
        max_sum = max(max_sum, last.val + first.val)
        last = last.next
        first = first.next
    return max_sum
