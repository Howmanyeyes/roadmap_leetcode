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
        


        sorted_words = [x for x in word_map.items()]
        sorted_words = sorted(sorted_words, key = lambda x: x[1], reverse = True)
        ans = []
        ans_nums = set()
        pre_ans = []
        for num in range(k):
            a = sorted_words[num][1]
            if sorted_words[num][1] in ans_nums:
                p = num - 1
                while sorted_words[p][1] == a:
                    pre_ans.append(sorted_words[p][0])
                    p += 1
                    if p - num - 1 > k:
                        break
                pre_ans = sorted(pre_ans, key = lambda x: ord(x[0][0]))
                for answer in pre_ans:
                    ans.append(answer)
            else:
                ans_nums.add(num)
                ans.append(sorted_words[num][0])
            if len(ans) >= k:
                break
            
        return ans[:k+1]

        print(1)

if __name__ == '__main__':
    s = Solution()
    s.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)