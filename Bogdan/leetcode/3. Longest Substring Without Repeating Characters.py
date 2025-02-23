class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # all_subs = set([s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)])
        #
        # max_len = 0
        # for i in all_subs:
        #     temp_dict = {}
        #     for j in i:
        #         if j not in temp_dict:
        #             temp_dict[j] = 1
        #         elif temp_dict[j] == 1:
        #             break
        #     if len(temp_dict) > max_len:
        #         max_len = len(temp_dict)
        # return max_len
        # all_subs = []
        # max_len = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         current_sub = s[i:j]
        #         if current_sub in all_subs:
        #             continue
        #         temp_dict = {}
        #         for k in current_sub:
        #             if k not in temp_dict:
        #                 temp_dict[k] = 1
        #             elif temp_dict[k] == 1:
        #                 break
        #         if len(temp_dict) > max_len:
        #             max_len = len(temp_dict)
        #         all_subs.append(current_sub)
        # return max_len

        # код по памяти и времени хуйня, поэтому я прочитал про скользящее окно

        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_len = max(max_len, right-left+1)

        return max_len




