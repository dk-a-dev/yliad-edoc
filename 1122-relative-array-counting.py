class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr=[]
        for item in arr2:
            while(item in arr1):
                arr.append(item)
                arr1.remove(item)
        for item in arr1:
            arr.append(item)
        return arr

a=Solution()
print(a.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))