#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(char_map[s[right]] + 1, left)
            char_map[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
        
# @lc code=end

