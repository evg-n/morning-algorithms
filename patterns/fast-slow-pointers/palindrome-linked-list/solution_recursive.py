class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rec_find_middle(s, f):
    if f and f.next:
        is_still_valid, right_part_node, is_forward_offset_required = rec_find_middle(s.next, f.next.next)
        if not is_still_valid:
            return (is_still_valid, right_part_node, is_forward_offset_required)
        
        if right_part_node is None:
            return (True, None, None)

        left_part_val = s.next.val if is_forward_offset_required else s.val
        if left_part_val != right_part_node.val:
            return (False, None, None)
        return (True, right_part_node.next, is_forward_offset_required)
    else:
        return (True, s.next, bool(f))


def palindrome(head):
    if not head.next:
        return True
    dummy = ListNode(0, head)    
        
    return rec_find_middle(dummy, dummy)[0]

