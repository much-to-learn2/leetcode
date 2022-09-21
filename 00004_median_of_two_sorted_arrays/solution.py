import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_length = len(nums1) + len(nums2)
        if merged_length % 2 == 0:
            target = merged_length / 2 + 1
        else:
            target = math.ceil(merged_length / 2)
        print(target)
        i, j, c = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            # consume one array entirely
            c += 1
            
            if nums1[i] < nums2[j]:
                current = nums1[i]
                i += 1
            else:
                current = nums2[j]
                j += 1
                
            if c == target:
                return self.calculate_median(merged_length, previous, current)
            
            previous = current
            print(current)
            
        if i < len(nums1) or j < len(nums2):
            rem = nums1[i:] if i < len(nums1) else nums2[j:]
            for n in rem:
                c += 1
                current = n
                if c == 1:
                    previous = current
                if c == target:
                    return self.calculate_median(merged_length, previous, current)
                previous = current
                print(n)
            
        return 1
    
    
    def calculate_median(self, merged_length, previous, current):
        if merged_length % 2 == 0:
            return (current + previous) / 2
        else:
            return current
                
