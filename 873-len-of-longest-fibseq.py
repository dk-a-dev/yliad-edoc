class Solution:
    def lenLongestFibSubseq(self, arr) -> int:
        n=len(arr)
        exists=set(arr)
        res=0
        for i in range(n):
            for j in range(i+1,n):
                a,b,l=arr[i],arr[j],2
                while a+b in exists:
                    a,b=b,a+b
                    l+=1
                if(l>2):
                    res=max(res,l)
        return res

a=Solution().lenLongestFibSubseq(eval(input()))