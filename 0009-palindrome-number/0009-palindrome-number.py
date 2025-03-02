class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Checking for Negative numbers which can not be palindromes
        if x < 0:
            return False
        # converting number to string and reversing and checking if its equals
        return str(x) == str(x)[::-1]