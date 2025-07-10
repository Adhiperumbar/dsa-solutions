class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        n=len(num)
        k=int(n/2)
        if n%2==0:
            med=(num[k-1]+num[k])/2
            return med
        else:
            return num[k]