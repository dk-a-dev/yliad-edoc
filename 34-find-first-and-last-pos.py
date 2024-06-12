class Solution:
    def searchRange(self, nums:int, target: int):
        arr=[]
        i=0
        if(target not in nums):
            return [-1,-1]
        while target in nums:
            arr.append(nums.index(target)+i)
            nums.remove(target)
            i+=1
        return [arr[0],arr[-1]]