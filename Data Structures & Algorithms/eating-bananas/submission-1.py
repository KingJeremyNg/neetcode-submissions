class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            middle = (left + right) // 2
            time = sum([math.ceil(pile / middle) for pile in piles])
            if time > h:
                left = middle + 1
            elif time <= h:
                right = middle - 1
                result = min(result, middle)

        return result
