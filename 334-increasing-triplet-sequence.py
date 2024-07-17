import math


class Solution:
    def increasingTriplet(self, nums) -> bool:
        l=len(nums)
        first=second=math.inf
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False
