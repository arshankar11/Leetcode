"""
Approach: Two Pointers/Brute-Force Search

Complexity:O(N2)O(N2)

Runtime: 3203ms Beats: 5.00%
Memory: 19.69MB Beats:95.10%


"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        # The two pointers approach
        while left < right:
            current_sum = nums[left] + nums[right]

            #Check the sum with the target
            if current_sum == target:
                return [left,right]
            
            elif left == (right - 1):
                left += 1
                right = len(nums) - 1
            else:
                right -= 1

        return None
        