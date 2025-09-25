def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head  # current item = head ie first item in the linked list
    prev = None  # previous item is None
    while curr:  # whilst current is not None ie in bounds
        nxt = curr.next  # temporary variable to save next item in the list as in 1 -> 2 before we overwrite the sequence
        curr.next = prev  # next item in the linked list is now the previous one
        prev = curr  # the previous item is now the item we were just on
        curr = nxt  # moves onto the next item in the linked list as in 1 -> 2
    return prev  # returns the reversed list