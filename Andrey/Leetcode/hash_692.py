"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/description/
"""

"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same
frequency by their lexicographical order.

"""

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        word_map = {}
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1
        
        sorted_words = sorted([x for x in word_map.items()], key = lambda y: y[1], reverse = True)
        ans = []
        sortable = []
        used_digits = set()
        for i in range(k):
            if sorted_words[i][0] in ans:
                continue
            
            digit = sorted_words[i][1]
            disp = 1
            sortable.append(sorted_words[i][0])
        
            while sorted_words[i+disp][1] == digit:
                sortable.append(sorted_words[i+disp][0])
                disp += 1
                if disp + i >= len(sorted_words):
                    break
        
            sortable.sort()
            for x in sortable:
                ans.append(x)
            
            sortable = []
        if len(ans) >= k:
            return ans[:k]
        return ans[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(["i","love","leetcode","i","love","coding"], 3))