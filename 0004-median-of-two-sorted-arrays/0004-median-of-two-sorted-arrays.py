class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list = nums1 + nums2
        final_list = sorted(final_list)
        length = len(final_list)
        result = 0
        if length % 2 == 0: 
            result = (final_list[length//2] + final_list[length//2 -1])/2
        else :
            result = final_list[length//2]
        return result