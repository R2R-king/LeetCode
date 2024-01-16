class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums2 = []
        for elem in nums:
            if elem not in nums2:
                nums2.append(elem)
        
        nums[:] = nums2

        return len(nums2)

        
        
         
        
    



a = Solution()

a.removeDuplicates([1, 1, 2])

        
            
        
            
      





