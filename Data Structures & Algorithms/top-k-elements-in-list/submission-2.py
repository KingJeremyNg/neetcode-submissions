class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sortedFreq = sorted(freq.items(), key=lambda item: item[1])

        result = []
        for i in range(len(sortedFreq) - 1, len(sortedFreq) - k - 1, -1):
            result.append(sortedFreq[i][0])

        return result
