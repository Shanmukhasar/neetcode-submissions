class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        seen = set()

        max_length , left = 0 , 0

        for right in range(n):

            while s[right] in seen:

                seen.remove(s[left])

                left = left + 1

            max_length = max(max_length , right - left + 1)

            seen.add(s[right])

        return max_length



        