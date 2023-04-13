# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # check both left and right children
        # if left side -> if left child, right side -> right child
        # if right child, right side needs needs left child
        # also need to have same values
        # need to check both sides at same time?
        #check left side -> store right side contents in stack?
        stackRight = []
        def checkLeft(node):
            if node == None:
                return None
            stackRight.append(node.val)
            if node.right:
                checkLeft(node.right)
            else:
                stackRight.append(None)
            if node.left:
                checkLeft(node.left)
            else:
                stackRight.append(None)
        def checkRight(node):
            if node == None:
                return None
            if stackRight[0] == node.val:
                stackRight.pop(0)
            else:
                return False
            if node.left:
                if stackRight[0] == "None" and node.right:
                    return False
                checkRight(node.left)
            else:
                if stackRight[0] == None:
                    stackRight.pop(0)
                else:
                    return False
            if node.right:
                if stackRight[0] == "None" and node.left:
                    return False
                checkRight(node.right)
            else:
                if stackRight[0] == None:
                    stackRight.pop(0)
                else:
                    return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        else:
            checkLeft(root.left)
            checkRight(root.right)
            return True if len(stackRight) == 0 else False

if __name__ == "__main__":
    # x = TreeNode(1, TreeNode(2, left=None, right=TreeNode(3)), TreeNode(2, left=None, right=TreeNode(3)))
    # x = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    x = TreeNode(1, left=None, right=TreeNode(2))
    w = Solution()
    w.isSymmetric(x)