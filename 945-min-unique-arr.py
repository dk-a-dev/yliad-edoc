class Solution:
    def checkUnique(self,nums):
        for i in range(0,len(nums)):
            if(nums.count(nums[i])==1):
                continue
            else:
                return False
        return True
    def minIncrementForUnique(self, nums) -> int:
        count=0
        while(not self.checkUnique(nums)):
            for i in range(0,len(nums)):
                if(nums.count(nums[i])==1):
                    continue
                else:
                    nums[i]+=1
                    count+=1
                    print(nums)
        return count

a=Solution().minIncrementForUnique(eval(input()))
print(a)