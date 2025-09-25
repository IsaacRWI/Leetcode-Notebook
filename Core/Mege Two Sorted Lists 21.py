class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1, list2):
    dummy = ListNode()  # dummy node in case both linked lists are empty
    tail = dummy  # tail is the linked list the elements in the list will be combined onto
    while list1 and list2:  # whilst list1 and list2 nodes are still not None  ie theyre still in the linked list
        if list1.val < list2.val:  # if list1 value is smaller than list2
            tail.next = list1  # next value in tail is the current node value for list1
            list1 = list1.next  # list1 node value becomes the next value in list1
        else:
            tail.next = list2  # next value in tail is the current node value for list2
            list2 = list2.next  # list2 node value becomes the next value in list2
        tail = tail.next  # moves the tail node to the next node that was just added list1 or 2
    if list1:  # after breaking out of the loop if list1 node value is still not None
        tail.next = list1  # adds the rest of list1 onto tail
    elif list2:
        tail.next = list2  # same for list2

    return dummy.next  # return tails excluding the dummy node