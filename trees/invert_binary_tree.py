class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        def invert(node):
            if node.left and node.right:
                tmp_l, tmp_r = node.left, node.right

                node.left = tmp_r
                node.right = tmp_l

                invert(node.left)
                invert(node.right)
            elif node.left or node.right:
                if node.left:
                    node.right = node.left
                    invert(node.left)
                    node.left = None
                elif node.right:
                    node.left = node.right
                    invert(node.right)
                    node.right = None
                else:
                    pass
            else:
                pass
                
            return node
            
        return invert(root)
                

if __name__ == "__main__":
    # node = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    node = TreeNode(2, left=TreeNode(3, left = TreeNode(1)))
    w = Solution()
    w.invertTree(node)