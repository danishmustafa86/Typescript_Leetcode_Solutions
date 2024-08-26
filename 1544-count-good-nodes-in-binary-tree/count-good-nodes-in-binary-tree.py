# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxval):
            if not node:
                return 0
            res = 1 if node.val >= maxval else 0
            maxval = max(maxval, node.val)
            res += dfs(node.left, maxval)
            res += dfs(node.right, maxval)
            return res
        return dfs(root, root.val)














# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def solve(root,val):
#             if root:
#                 k = solve(root.left, max(val,root.val)) + solve(root.right, max(val,root.val))
#                 if root.val >= val:
#                     k+=1
#                 return k
#             return 0
#         return solve(root,root.val)