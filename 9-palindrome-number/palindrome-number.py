class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign= -1 if x<0 else 1
        num=x
        rev=0
        while num>0:
            ld=num%10
            rev=rev*10+ld
            num=num//10
        rev*=sign
        if rev==x:
            return True
        else:
            return False
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        