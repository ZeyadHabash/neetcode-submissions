class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I think my initial thought of best solution would be to sort the list first
        # then handle it kinda like sorted twosum
        # but we'll prob do nested lube so it'll be O(n^2)

        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # this is here to skip duplicates
            front, back = i+1, len(nums) - 1
            while front < back:
                num_sum = nums[i] + nums[front] + nums[back]
                if num_sum > 0:
                    back -= 1
                elif num_sum < 0:
                    front += 1
                else:
                    result.append([nums[i], nums[front], nums[back]])
                    front += 1
                    # we need a way to exclude duplicates here too
                    while front < back and nums[front] == nums[front-1]:
                        front += 1

                


        return result