# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TestSolution(object):
    def mergeTwoLists(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # For both list, we compare each ListNode's value
        # Whichever is smaller will go into the dummy variable "merged"
        # and be updated from a temporary variable "tmp"
        # Dummy variable starts with empty node of 0, we then return merged.next
        # Runtime: O(N)
        # Space: O(1)
        # 
        merged = tmp = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        if list1:
            tmp.next = list1
        else:
            tmp.next = list2
        return merged.next

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    TestSolution.mergeTwoLists(l1, l2)

