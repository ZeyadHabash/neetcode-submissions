class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We can do better time wise at the cost of some space
        # Using a hashmap we can prob save the compliment of each number as a key
        # Then check that against the remaining numbers as we go

        # O(n) time and space complexities

        compliments = {}
        for i in range(len(nums)):
            if nums[i] in compliments:
                return [compliments[nums[i]], i]
            compliments[target-nums[i]] = i

        return []