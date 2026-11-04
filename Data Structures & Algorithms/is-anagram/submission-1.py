class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        if s == t:
            return True

        # sort then check if theyre the same
        # O()

        # sorting each string takes maybe O(nlogn) (?)
        # equality takes another O(n) as it compares each character
        if sorted(s) == sorted(t):
            return True

        # so this solution is O(nlogn)

        return False
