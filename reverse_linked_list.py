class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TestSolution(object):
    def test_reverseList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # use recursion to reverse List
        if head == None:
            return None

        reversed_ = ListNode(head.val, None)
        print(reversed_)

        def reversed(node, rev):
            if node.next:
                rev = ListNode(node.next.val, rev)
                rev = reversed(node.next, rev)
            return rev
        # important to reference for local variables for persistence
        res = reversed(head, reversed_)
        # while res:
        #     print(res.val)
        #     res = res.next
        return res


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    TestSolution.test_reverseList(l1)
