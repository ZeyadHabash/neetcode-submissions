class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        curr_substring = ""
        for char in s:
            if char in curr_substring:
                maxLength = max(maxLength, len(curr_substring))
                while char in curr_substring:
                    curr_substring = curr_substring[1:]
            curr_substring += char
        
        return max(len(curr_substring), maxLength)
            