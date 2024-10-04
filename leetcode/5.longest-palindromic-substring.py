#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        if len(s)==0:
            return ""

        def parallel(s,i,j):
            while (i>=0)and(j<len(s))and (s[i]==s[j]):
                i=i-1
                j=j+1
            return s[i+1:j]
        long =""
        for k in range(len(s)):
            odd = parallel(s,k,k)
            even = parallel(s,k,k+1)
            if len(odd)>len(long): long=odd
            if len(even)>len(long): long= even
        return long
# @lc code=end

