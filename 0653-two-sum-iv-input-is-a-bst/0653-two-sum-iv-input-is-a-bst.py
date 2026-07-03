# BEST: BST Iterator Approach
class Solution(object):
    def findTarget(self, root, k):
        if not root:
            return False
        
        left_stack = []
        right_stack = []
        
        curr = root
        while curr:
            left_stack.append(curr)
            curr = curr.left
        
        curr = root
        while curr:
            right_stack.append(curr)
            curr = curr.right
        
        while left_stack and right_stack:
            left_node = left_stack[-1]
            right_node = right_stack[-1]
            
            if left_node == right_node:
                break
            
            curr_sum = left_node.val + right_node.val
            
            if curr_sum == k:
                return True
            elif curr_sum < k:
                node = left_stack.pop()
                curr = node.right
                while curr:
                    left_stack.append(curr)
                    curr = curr.left
            else:
                node = right_stack.pop()
                curr = node.left
                while curr:
                    right_stack.append(curr)
                    curr = curr.right
        
        return False