
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        freq = Counter(nums)

        counter = [[] for _ in range(n + 1)]

        for num , count in freq.items():

            counter[count].append(num)

        result = []

        for i in range(len(counter) - 1 , 0 , - 1):

            for num in counter[i]:

                result.append(num)

                if len(result) == k:

                    return result


        