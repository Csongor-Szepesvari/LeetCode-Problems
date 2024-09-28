# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # on each node, we pass down a less than and greater than value
        # we return the conditional statement of the lower section being bst and if it fits

        def recursion(root, greater_than, less_than):
            if root == None:
                return True

            if root.val <= greater_than or root.val >= less_than:
                return False

            return recursion(root.left, less_than=root.val, greater_than=greater_than) and recursion(root.right, less_than=less_than, greater_than=root.val)

        return recursion(root, greater_than=float('-inf'), less_than=float('inf'))