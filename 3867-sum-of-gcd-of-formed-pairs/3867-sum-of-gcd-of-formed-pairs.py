class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        prefixGcd = []
        mx = 0

        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(self.gcd(num, mx))

        prefixGcd.sort()

        ans = 0
        i, j = 0, len(prefixGcd) - 1

        while i < j:
            ans += self.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans