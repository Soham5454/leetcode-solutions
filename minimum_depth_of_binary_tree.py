from collections import deque

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # if it's a leaf node, return immediately!
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
