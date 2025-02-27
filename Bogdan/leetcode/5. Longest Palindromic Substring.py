class Solution:
    def longestPalindrome(self, s: str) -> str:
        #
        # max_pd = ''
        # for left_ptr in range(len(s)):
        #
        #     right_ptr = len(s) - 1
        #
        #     while right_ptr>left_ptr and s[left_ptr] != s[right_ptr]:
        #         right_ptr -= 1
        #
        #     temp_pol_str= s[left_ptr:right_ptr]
        #
        #     while s[left_ptr] == s[right_ptr] or left_ptr < right_ptr:
        #         left_ptr += 1
        #         right_ptr -= 1
        #
        #     if left_ptr >= right_ptr:
        #         max_pd = max(max_pd, temp_pol_str, key=len) код хуйня ибо не покрыл один тест, так как пропустил его

        if len(s) == 0:
            return ""

        max_pd = ''
        def pd_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            odd_pd = pd_around_center(i, i)
            even_pd = pd_around_center(i, i+1)

            max_pd = max(odd_pd, even_pd, max_pd, key=len)

        return max_pd



