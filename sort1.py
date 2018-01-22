#!/usr/bin/env python

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    even = False
    if (m+n)%2 == 0:
        even = True
    while m > 1 and n > 1:
        if nums1[m/2] > nums2[n/2]:
            if m % 2 == 0:
                nums1 = nums1[:m/2]
            else:
                nums1 = nums1[:1+(m/2)]
            if n % 2 == 0:
                nums2 = nums2[n/2:]
            else:
                nums2 = nums2[1+(n/2):]
        else:
            if m % 2 == 0:
                nums1 = nums1[m/2:]
            else:
                nums1 = nums1[(m/2)-1:]
            if n % 2 == 0:
                nums2 = nums2[:n/2]
            else:
                nums2 = nums2[:(n/2)-1]
        m = len(nums1)
        n = len(nums2)
    if m == 1:
        pass

l1 = [1,2,3,4,5,6,7,8]
l2 = [9,10,11,12]
print findMedianSortedArrays(l1,l2)
l3 = [1,7,8,9,10,11,11,11,11,11]
l4 = [2,2,2,3,3,3,3,3,3,15,15]
print findMedianSortedArrays(l3,l4)
l3 = [1,3]
l4 = [2,3]
print findMedianSortedArrays(l3,l4)
