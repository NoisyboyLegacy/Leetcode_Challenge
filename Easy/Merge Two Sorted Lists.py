
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next

def convert_to_linked_list(lst):
    dummy = ListNode()
    ptr = dummy
    for i in lst:
        ptr.next = ListNode(i)
        ptr = ptr.next
    return dummy.next
def convert_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

list1 = convert_to_linked_list([1,2,4])
list2 = convert_to_linked_list([1,3,4])
merged_list = mergeTwoLists(list1, list2)
print(convert_to_list(merged_list))