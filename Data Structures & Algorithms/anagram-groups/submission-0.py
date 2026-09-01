from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            l=list(word)
            s=''.join(sorted(word))
            d[s].append(word)
        l=[]
        for num in d:
            l.append(d[num])
        return l

        