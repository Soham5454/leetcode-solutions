class Solution:
    def postorderTraversal(self, root):
        result = []
        
        def helper(node):
            if node is None:
                return
            helper(node.left)
            helper(node.right)
            result.append(node.val)  # ← inside helper, after both calls
        
        helper(root)
        return result
