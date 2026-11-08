class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        # n
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1

        sortingList = [[] for _ in range(len(nums))]
        # + n
        for item in freqMap:
            sortingList[freqMap[item]-1].append(item)

        result = []
        # + n
        for i in range(len(nums) - 1, -1, -1):
            if k <= 0:
                break
            if sortingList[i]:
                for num in sortingList[i]:
                    result.append(num)
                    k -= 1


        # so this answer is O(n) time
        return result