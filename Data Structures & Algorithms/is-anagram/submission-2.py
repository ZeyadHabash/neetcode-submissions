class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        if s == t:
            return True


        # a better solution would be to use a hashmap with char as key and frequency as value for an O(n) time complexity solution
        # this still doesnt have O(1) space as it uses a hashmap

        freq_map  = {}

        for c in s:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1
        
        for c in t:
            if c in freq_map:
                freq_map[c] -= 1
                if freq_map[c] <= 0:
                    freq_map.pop(c)
            else:
                return False
        
        if len(freq_map) <= 0:
            return True


        return False