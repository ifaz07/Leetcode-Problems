class Solution(object):
    
    def isSubtree(self, root, subRoot):
        if not root:
            return False
        if not subRoot:
            return True
        
        if self._is_same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def _is_same(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        return self._is_same(node1.left, node2.left) and self._is_same(node1.right, node2.right)