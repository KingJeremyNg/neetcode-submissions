class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = math.inf

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= nums[right]:
                left = middle + 1
            elif nums[middle] <= nums[right]:
                right = middle - 1
            result = min(result, nums[middle])

        return result
