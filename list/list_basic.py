
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def demo_reverse_list():
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c
    r_a = reverseList(a)
    while r_a:
        print(r_a.val)
        r_a = r_a.next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next

def demo_merge_two_lists():
    a = ListNode(3)
    b = ListNode(40)
    c = ListNode(50)
    a.next = b
    b.next = c

    a1 = ListNode(30)
    b1 = ListNode(41)
    c1 = ListNode(45)
    a1.next = b1
    b1.next = c1

    merged_list = mergeTwoLists(a, a1)
    while merged_list:
        print(merged_list.val)
        merged_list = merged_list.next

def hasCycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def demo_has_cycle():
    a = ListNode(3)
    b = ListNode(40)
    c = ListNode(50)
    a.next = b
    b.next = c
    print(hasCycle(a))
    c.next = a
    print(hasCycle(a))

if __name__ == "__main__":
    demo_has_cycle()