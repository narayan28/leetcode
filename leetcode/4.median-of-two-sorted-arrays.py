#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=nums1+nums2
        arr.sort()
        l=len(arr)
        if l%2==1:
            return arr[(l-1)//2]
        else:
            return (arr[(l-2)//2]+arr[l//2])/2
# @lc code=end

