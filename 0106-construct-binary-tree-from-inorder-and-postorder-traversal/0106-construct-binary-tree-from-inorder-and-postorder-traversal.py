# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        self.postorder_index = len(postorder) - 1
        self.inorder_map = {}
        
        for index, value in enumerate(inorder):
            self.inorder_map[value] = index
        
        return self._build_tree(postorder, 0, len(inorder) - 1)
    
    def _build_tree(self, postorder, left, right):
        if left > right:
            return None
        
        root_val = postorder[self.postorder_index]
        self.postorder_index -= 1
        
        root = TreeNode(root_val)
        root_index = self.inorder_map[root_val]
        
        root.right = self._build_tree(postorder, root_index + 1, right)
        root.left = self._build_tree(postorder, left, root_index - 1)
        
        return root