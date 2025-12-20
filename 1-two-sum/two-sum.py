class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}
        for i in range(len(nums)):
            if (target-nums[i]) not in has:
                has[nums[i]] = i
            else:
                return has[target - nums[i]],i 
