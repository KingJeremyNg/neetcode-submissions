class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = max(nums)

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= nums[right]:
                left = middle + 1
            if nums[middle] < nums[right]:
                right = middle - 1
            result = min(result, nums[middle])

        return result
