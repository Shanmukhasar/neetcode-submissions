class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        result = ''

        global_max = 0

        def palindrome(l , r):

            res = ''

            max_len = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:

                res = s[l : r + 1]

                max_len = max(max_len , r - l + 1)

                l = l - 1

                r = r + 1

            return res , max_len

        for i in range(n):

            odd_string , odd_length = palindrome(i , i)

            even_string , even_length = palindrome(i , i + 1)

            if odd_length >= even_length and odd_length > global_max:

                result = odd_string

                global_max = odd_length

            elif even_length > odd_length and even_length > global_max:

                result = even_string

                global_max = even_length

        return result

        


        