class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break

            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue

            j = i+1
            k = n-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans