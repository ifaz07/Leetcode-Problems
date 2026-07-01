class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        current = root
        
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            else:
                return current
        
        return None