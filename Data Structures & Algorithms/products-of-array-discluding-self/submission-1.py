class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first instinct is to get the product of everything in one loop
        # then in the next you just divide by the current (unless it's 0)
        
        # but then the follow up says solve it in O(n) without division
        # thats prob where the real challenge is

        # iterating over the entire loop then getting the product for each index is an O(n^2) Solution, not feasible
        # maybe we can store the product so far in an array as we go? 
        # do this with a pointer from front and pointer from back then multiply both and thats your result? 
        # will attempt this Solution

        # prefix_product, postfix_product = [1] * len(nums), [1] * len(nums)

        # for i in range(1, len(nums)):
        #     prefix_product[i] = prefix_product[i-1] * nums[i-1]

        # for i in range(len(nums)-2, -1, -1):
        #     postfix_product[i] = postfix_product[i+1] * nums[i+1]

        # result = [0] * len(nums)
        # for i in range(len(result)):
        #     result[i] = prefix_product[i] * postfix_product[i]
        

        # this should be O(n)

        # To save space we can do this in place instead of having 3 arrays
        n = len(nums)
        result = [1] * n
        prefix, suffix = 1, 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result