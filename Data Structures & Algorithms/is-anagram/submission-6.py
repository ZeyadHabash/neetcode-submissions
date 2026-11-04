class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # best solution would prob be doing both s and t passes in one loop
        # we are sure that they have the same length n so we can use that

        n = len(s)

        # uses 2 hashmaps instead of 1 but we're already limited by the size of the alphabet
        # so we're not trading away complexity its kinda small already
        s_letters = {}
        t_letters = {}

        for i in range(n):
            if s[i] in s_letters:
                s_letters[s[i]] += 1
            else:
                s_letters[s[i]] = 1
            if t[i] in t_letters:
                t_letters[t[i]] += 1
            else:
                t_letters[t[i]] = 1
        
        return s_letters == t_letters