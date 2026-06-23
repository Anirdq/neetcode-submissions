class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        xd={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in xd:
                return [xd[diff], i]
            else:
                xd[n]=i
        return
                
                