class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def helper(node):
            if node is None:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return result
