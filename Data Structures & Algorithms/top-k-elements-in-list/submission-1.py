class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first solution that comes to mind:
        # create a freq map of each number (number is key, frequency is value)
        # sort freq map by value and select top k
        result = []
        freqMap = {}

        # n
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1

        # + nlogn for sorting
        sortedVal = list(freqMap.items())
        sortedVal.sort(key=lambda x:x[1],reverse=True)

        # + k
        for i in range(k):
            result.append(sortedVal[i][0])

        # so this is and O(nlogn) solution, we can prob do better if we avoid sorting and just find max k using 1 loop
        return result