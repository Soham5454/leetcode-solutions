class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)
