class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=0
        foo=[]
        for candie in candies:
            if candie>max:
                max=candie
        
        for candie in candies:
            if candie+extraCandies>=max:
                foo.append(True)
            else:
                foo.append(False)
        
        return foo

