from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = defaultdict(list)

        for word in strs:

            sorted_word = ''.join(sorted(list(word)))

            hash_map[sorted_word].append(word)

        output = []

        for words in hash_map:

            output.append(hash_map[words])

        return output




        