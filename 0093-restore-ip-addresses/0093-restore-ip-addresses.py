class Solution(object):
    def restoreIpAddresses(self, s):

        result = []
        n = len(s)

        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    if n - k > 3:
                        continue
                    
                    part1 = s[:i]
                    part2 = s[i:j]
                    part3 = s[j:k]
                    part4 = s[k:]
                    
                    if self.is_valid(part1) and self.is_valid(part2) and \
                       self.is_valid(part3) and self.is_valid(part4):
                        result.append('.'.join([part1, part2, part3, part4]))
        
        return result
    
    def is_valid(self, segment):
        if not segment:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        return 0 <= int(segment) <= 255