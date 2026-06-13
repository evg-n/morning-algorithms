class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    """Build a singly linked list from an iterable; return the head node."""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    """Read a linked list back into a Python list (for assertions/printing)."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def find_node_by_idx(head, idx):
    
    while idx:
        idx -= 1
        head = head.next
    return head

def build_cycle(values, idx):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = find_node_by_idx(dummy.next, idx)
    return dummy.next

