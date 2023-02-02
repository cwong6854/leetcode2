# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        removeElement = curr = ListNode()
        while head:
            print(head.val)
            # if head.val == val:
            if head.val == val:
                head = head.next
                curr.next = head
            else:
                curr.next = head
                curr = head
                head = head.next
        return removeElement.next

if __name__ == "__main__":
    lst = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
    target = 6
    
    test = Solution()
    test.removeElements(lst, target)