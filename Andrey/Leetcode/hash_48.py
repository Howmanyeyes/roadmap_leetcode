"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
using all the original letters exactly once.

I can map every word and then iterate through maps to do something, idk, i'm very tilted

I remembered about ord(str) function, but unfortunatelly it doesn't help here. I can think of only
one other super inefficient solution, i won't even implement it. I am so tired i want only to smoke
and lie down.

For now i will look solution and try implementing it myself.

BLIIAAAAATTTT I forgot about sorting words, i fucking hate myself
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        classes: dict[str, list] = {}
        for word in strs:

            word_sorted = ''.join(sorted(word))
            if word_sorted in classes:
                classes[word_sorted].append(word)
            else:
                classes[word_sorted] = [word]
        return [*classes.values()]
        

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))