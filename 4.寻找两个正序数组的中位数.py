class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range (len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if len(nums1)%2 == 0:
            a = nums1[int(len(nums1)/2)]
            b = nums1[int(len(nums1)/2)-1]
            return (a+b)/2
        if len(nums1)%2 == 1:
            a = int(len(nums1)/2)
            return nums1[a]
        if len(nums1) == 0:
            return 0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    C = Solution()
    median = C.findMedianSortedArrays(nums1, nums2)
    print(median)
    nums3 = [1,2]
    nums4 = [3,4]
    median2 = C.findMedianSortedArrays(nums3, nums4)
    print(median2)