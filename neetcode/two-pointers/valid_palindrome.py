class Solution:
    def isPalindrome(self, s: str) -> bool:
        # solution 1
        # using built in funcs
        # O(N) time, O(N) memory for new string

        #         newStr = ""

        #         for c in s:
        #             if c.isalnum():
        #                 newStr += c.lower()

        #         return newStr == newStr[::-1]

        # solution 2
        # two pointers
        # avoid using extra memory
        # avoid using built in python funcs
        # O(1) memory complexity
        # O(N) time complexity
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.isAlphaNum(s[l]):
                l += 1

            while r > l and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def isAlphaNum(self, char):
        isLowerCase = (ord(char) >= ord('a')) and (ord(char) <= ord('z'))
        isUpperCase = (ord(char) >= ord('A') and ord(char) <= ord('Z'))
        isNumber = (ord(char) >= ord('0') and ord(char) <= ord('9'))
        return isLowerCase or isUpperCase or isNumber
