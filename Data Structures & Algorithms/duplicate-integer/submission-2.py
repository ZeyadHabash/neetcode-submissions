class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Better solution O(n)
        # Create a hashmap
        # check hashmap
        # if exists return true
        # if doesnt insert into hashmap

        hashMap = {}

        for i in nums:
            if hashMap.get(i):
                return True;
            else:
                hashMap[i] = 1;
        
        return False