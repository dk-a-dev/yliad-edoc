class Solution:
    def compress(self, chars) -> int:
        arr=[]
        count=0
        setLst=sorted(set(chars))
        for i in setLst:
            count=chars.count(i)
            if count==1:
                arr.append(i)
            else:
                arr.append(i)
                arr.extend(list(str(count)))
        print(arr)
        return len(arr)

if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c"]))