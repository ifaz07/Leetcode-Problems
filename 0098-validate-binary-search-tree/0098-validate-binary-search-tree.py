class Solution(object):
    def isValidBST(self, root):
        return self.checkBST(root, float('-inf'), float('inf'))
    
    def checkBST(self, node, lower, upper):
        if not node:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
        
        return (self.checkBST(node.left, lower, node.val) and 
                self.checkBST(node.right, node.val, upper))