"""
Approach: Hash Table (or Dictionary)

Runtime: 0ms Beats:100.00%
Memory: 20.49MB Beats:41.53%

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  #Value : index

        #Iterate over nums dictionary
        for i,num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement],i]
            
            seen[num] = i
        
        return[]