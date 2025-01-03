# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# how to process inorder?
# process left, add middle, process right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def process(root):
            if root == None:
                return []
            if root.left == None and root.right == None:
                return [root.val]

            
            return process(root.left) + [root.val] + process(root.right)
        
        self.flat = process(root)
        self.index = -1
        self.max_index = len(self.flat)-1

    def next(self) -> int:
        self.index += 1
        return self.flat[self.index]

    def hasNext(self) -> bool:
        return self.index < self.max_index
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()