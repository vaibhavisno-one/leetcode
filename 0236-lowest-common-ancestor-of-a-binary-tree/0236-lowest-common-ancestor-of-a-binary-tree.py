# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        ans=None

        def dfs(root):
            nonlocal ans

            if not root:
                return 0


            left=dfs(root.left)
            right=dfs(root.right)

            own=0

            if root is p or root is q:
                own=1

            total=own+left+right

            if total==2 and ans is None:
                ans =root

            return total

        dfs(root)

        return ans