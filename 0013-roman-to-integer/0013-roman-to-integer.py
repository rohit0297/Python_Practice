class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        total = 0
        # Loop through each character in the roman numeral string
        for i in range(len(s)):
            # If curent value is less than the next value, subtract the current value
            if i + 1 < len(s) and roman_num[s[i]] < roman_num[s[i+1]]:
                total -= roman_num[s[i]]
            else:
                #otherwise, add the current value
                total += roman_num[s[i]]

        return total