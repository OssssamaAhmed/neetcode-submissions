class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        pairs = []
        result = []

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        for num, cnt in count.items():
            pairs.append([cnt, num])

        pairs.sort(reverse=True)

        for i in range(k):
            result.append(pairs[i][1])

        return result
        