from helpers.linked_list import build, to_list

def swap_list(node):
    prev, curr, last = None, node, node.next
    while True:
        curr.next = prev
        if not last:
            break
        prev, curr, last = curr, last, last.next
    return curr


def palindrome(head):
    if not head.next:
        return True
    dummy = ListNode(0, head)
    
        
    slow, fast = dummy, dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    mid.next = swap_list(mid.next)
    
    first = head
    second = mid.next

    while second and first.val == second.val:
        first = first.next
        second = second.next
    

    mid.next = swap_list(mid.next)

    return not second


if __name__ == "__main__":
    print(to_list(swap_list(swap_list(build([5, 4, 7, 9])))))
