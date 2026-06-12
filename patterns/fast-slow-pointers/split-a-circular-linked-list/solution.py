def split_circular_linked_list(head):  
    slow, fast = head, head.next
    while fast != head and fast.next != head:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow
    right_head = mid.next
    
    prev, curr = None, right_head
    while curr != head:
        curr, prev = curr.next, curr
    prev.next = right_head
    
    mid.next = head
    return [head,right_head]
