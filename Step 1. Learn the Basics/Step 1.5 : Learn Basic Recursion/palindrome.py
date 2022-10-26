# https://leetcode.com/problems/valid-palindrome/

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = str(re.sub('[\W_]', '', s)).lower()
        if(s==s[::-1]):
            return True
        else:
            return False
