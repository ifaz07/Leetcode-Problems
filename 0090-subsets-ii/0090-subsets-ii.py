class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        
        self._backtrack(nums, 0, [], result)
        return result
    
    def _backtrack(self, nums, start, path, result):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            self._backtrack(nums, i + 1, path, result)
            path.pop()