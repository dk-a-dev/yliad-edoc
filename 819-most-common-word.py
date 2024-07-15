class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        k=",.;?!'"
        para=paragraph.lower()
        for char in k:
            para=para.replace(char,' ')
        
        countDict=collections.Counter(para.split())
        print(countDict)
        print(para)
        word=""
        freq=0
        for item,frq in countDict.items():
            if item not in banned and frq>freq:
                freq=frq
                word=item
        
        return word
