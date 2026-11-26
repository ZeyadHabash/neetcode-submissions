class Solution:
    def searchHelper(self, nums, left, right, target) -> int:
        if left > right:
            return -1
        mid = (right - left) // 2 + left
        val = nums[mid]
        if target == val:
            return mid
        if target < val:
            return self.searchHelper(nums, left, mid- 1, target)
        if target > val:
            return self.searchHelper(nums, mid + 1, right, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, 0, len(nums) - 1, target)
