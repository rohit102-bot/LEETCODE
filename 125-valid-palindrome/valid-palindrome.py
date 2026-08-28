class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch.lower() for ch in s if ch.isalnum())
        n=len(s)
        l=0
        r=n
        while l<r:
            if s[l]!=s[r-1]:
                return False
            else:
                l+=1
                r-=1
        else:
            return True
            
            