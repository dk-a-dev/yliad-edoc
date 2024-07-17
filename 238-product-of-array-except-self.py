class Solution:
    def productExceptSelf1(self, nums):
        arr=[]
        for i in range(len(nums)):
            prod=1
            for j in range(len(nums)):
                if(i==j):
                    continue
                else:
                    prod*=nums[j]
            arr.append(prod)
        return arr
    
    def productExceptSelf2(self, nums):
        arr=[]
        length=len(nums)
        for num in nums:
            pro*=num
        for i in range(length):
            try:
                arr.append(pro/nums[i])
            except:
                print("Divide By Zero")
        return arr