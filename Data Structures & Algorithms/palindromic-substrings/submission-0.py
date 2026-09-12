class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)

        result = 0

        def count_palindromes(l , r):

            count = 0

            while l >= 0 and r < n and s[l] == s[r]:

                count = count + 1

                l = l - 1

                r = r + 1

            return count

        for i in range(n):

            odd_res = count_palindromes(i , i)

            even_res = count_palindromes(i , i + 1)

            result = result + odd_res + even_res

        return result

            
        