def count_cycle_length(head):
   if not head or not head.next:
      return -1
   slow, fast = head.next, head.next.next
   
   while slow != fast and fast and fast.next:
      slow = slow.next
      fast = fast.next.next

   if not fast or not fast.next:
      return 0
   
   slow = head
   while slow != fast:
      slow = slow.next
      fast = fast.next
   
   curr, cnt = fast.next, 1
   while curr != fast:
      curr = curr.next
      cnt += 1
      
   return cnt
