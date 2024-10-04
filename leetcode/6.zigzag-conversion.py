#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows==1) or (numRows>=len(s)): 
            return s
        st1 = {}
        for i in range(numRows):
            st1[i]=''
        i=0
        while s:
            while i<numRows:
                st1[i]=st1[i]+s[0]
                s = s[1:]
                if len(s)==0: break
                i=i+1
            if len(s)==0: break
            i=i-1
            while i>0:
                i=i-1
                st1[i]=st1[i]+s[0]
                s = s[1:]
                if len(s)==0: break
            i=i+1
            if len(s)==0: break
        return ''.join(st1.values())
        
# @lc code=end

