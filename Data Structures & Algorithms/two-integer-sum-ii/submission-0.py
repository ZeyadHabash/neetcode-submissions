class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) space means no hashtable
        # but the array is sorted so we can just use a back pointer and a front pointer?
        # from the back start passing over each index till we find numbers[back] <= target
        # then start moving front pointer till numbers[back] + numbers[front] > target

        front = 0
        back = len(numbers) - 1

        while front < back:
            num_sum = numbers[front] + numbers[back]

            if num_sum > target:
                back -= 1
            elif num_sum < target:
                front += 1
            else:
                return [front + 1, back + 1] # +1 bec the array is 1 indexed

        return []