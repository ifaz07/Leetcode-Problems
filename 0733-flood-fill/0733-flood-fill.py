# Complete solution with all edge cases handled
class Solution(object):
    def floodFill(self, image, sr, sc, color):

        # Edge case 1: Empty image
        if not image or not image[0]:
            return image
        
        rows, cols = len(image), len(image[0])
        
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
            return image
        
        original_color = image[sr][sc]
        
        if original_color == color:
            return image
        
        from collections import deque
        queue = deque([(sr, sc)])
        image[sr][sc] = color
        
        # Optimization: Use single list of directions
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    image[nr][nc] == original_color):
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
        return image