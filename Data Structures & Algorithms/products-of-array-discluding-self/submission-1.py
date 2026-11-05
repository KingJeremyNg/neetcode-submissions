class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = []
        maxmult = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                results.append(math.prod(nums[:i] + nums[i + 1 :]))
            else:
                results.append(int(maxmult / nums[i]))
        return results
