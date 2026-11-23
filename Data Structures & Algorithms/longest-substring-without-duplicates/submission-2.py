class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        # curr_substring = ""
        # for char in s:
        #     if char in curr_substring:
        #         maxLength = max(maxLength, len(curr_substring))
        #         while char in curr_substring:
        #             curr_substring = curr_substring[1:]
        #     curr_substring += char

        # using sets and indices here would be a lott more efficient than using subsets and strings
        curr_substring = set()
        leftmost_char_idx = 0
        for i in range(len(s)):
            while s[i] in curr_substring:
                curr_substring.remove(s[leftmost_char_idx])
                leftmost_char_idx += 1
            curr_substring.add(s[i])
            maxLength = max(maxLength, i-leftmost_char_idx+1)
        
        return max(len(curr_substring), maxLength)
            