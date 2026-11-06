class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                    continue
                if nums[j] + nums[k] > target:
                    k -= 1
                    continue
                if nums[j] + nums[k] == target:
                    combo = [nums[i], nums[j], nums[k]]
                    if combo not in result:
                        result.append(combo)
                    j += 1
        return result
