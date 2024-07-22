from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # POSSIBLE THREE WAYS TO SOLVE: DFS, BFS, Iterative DFS
        # Intuition:
        # at each node visit, add + 1 and return
        # with no nodes -> depth should equal to 0
        # do DFS

        # Method: 
        # recursively visit left and right node, max between the two
        # create a dfs function

        # Time complexity: 
        # O(n) for each node inside the tree
        
        # Space complexity: 
        # O(n) worst case

        def dfsDepth(node):
            if not node:
                return 0
            return 1 + max(dfsDepth(node.left), dfsDepth(node.right))
        
        def bfsDepth(node):
            if not node:
                return 0
            
            level = 0
            q = deque([root])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1
            return level
        def bfsDepth(node):
            if not node:
                return 0
            
            level = 0
            q = deque([root])
            while q:
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level += 1
            return level
        def dfsIterative(node):
            if not node:
                return 0
            stack = [[node, 1]] # node, depth
            level = 0
            while len(stack) > 0:
                for i in range(len(stack)):
                    node, depth = stack.pop()
                    if node:
                        level = max(level, depth)
                        stack.append([node.left, depth + 1])
                        stack.append([node.right, depth + 1])
            return level
        return dfsIterative(root)
        # return bfsDepth(root)
        # return dfsDepth(root)
if __name__ == "__main__": 
    solution = Solution().maxDepth
    example = TreeNode(3, TreeNode(2), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert(solution(example)==3)
    print("All test cases passed!")
