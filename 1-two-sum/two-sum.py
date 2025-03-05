class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        for i in range(0,len(nums),1):
            for j in range(i+1,len(nums),1):
                if(nums[i]+nums[j]==target):
                    l=list()
                    l=[i,j]
                    return l
        