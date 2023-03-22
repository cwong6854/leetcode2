# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def leftLower(node, parent, currParent, side):
        #     if not node:
        #         return True

        #     if side == "right":
        #         return node.val < currParent.val and node.val > parent.val and leftLower(node.left, parent, node, side) and rightGreater(node.right, parent, node, side)

        #     return node.val < parent.val and node.val < currParent.val and leftLower(node.left, parent, node, side) and rightGreater(node.right, parent, node, side)
        
        # def rightGreater(node, parent, currParent, side):
        #     if not node:
        #         return True
        #     if side == "left":
        #         return node.val > currParent.val and node.val < parent.val and leftLower(node.left, parent, node, side) and rightGreater(node.right, parent, node, side)
            
        #     return node.val > parent.val and node.val > currParent.val and leftLower(node.left, parent, node, side) and rightGreater(node.right, parent, node, side)

        # def dfs(node, parent, child):
        #     if parent == None and child == None:
        #         pass
        #     if leftLower(node.left, node, node, "left") and rightGreater(node.right, node, node, "right"):
        #         return True
        #     else:
        #         return False
            
        # return dfs(root, None, None)
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        return valid(root, float("-inf"), float("inf"))

if __name__ == "__main__":
    # x = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    # x = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
    x = TreeNode(32, left=TreeNode(26, left=TreeNode(19, left=TreeNode(27), right=None), right=None), right=TreeNode(46, left=None, right=TreeNode(57)))
    w = Solution()
    print(w.isValidBST(x))