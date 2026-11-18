class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers, one from front and one from back and compare each character

        ptr1 = 0
        ptr2 = len(s) - 1
    
        while ptr1 <= ptr2:
            while ptr1 <= ptr2 and not s[ptr1].isalnum():
                ptr1 += 1
            while ptr1 <= ptr2 and not s[ptr2].isalnum():
                ptr2 -= 1
        
            if ptr1 > ptr2: 
                break

            if s[ptr1].lower() != s[ptr2].lower():
                return False
            ptr1 += 1
            ptr2 -= 1
    
        return True 