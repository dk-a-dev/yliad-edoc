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

    def productExceptSelf(self, nums):
        length=len(nums)
        arr=[1]*length
        pre=[1]*length
        suff=[1]*length
        print(arr,pre,suff)

        for i in range(1,length):
            pre[i]=pre[i-1]*nums[i-1]
            print(pre)

        for j in range(length-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]
            print(suff)

        for m in range(0,length):
            arr[m]=pre[m]*suff[m]
        return arr
    
    