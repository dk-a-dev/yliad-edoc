class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen=min(len(word1),len(word2))
        newStr=""
        for i in range(0,minlen):
            newStr+=word1[i]+word2[i]
        
        if(len(word1)>len(word2)):
            return newStr+word1[minlen:]
        elif(len(word1)<len(word2)):
            return newStr+word2[minlen:]
        else:
            return newStr
    