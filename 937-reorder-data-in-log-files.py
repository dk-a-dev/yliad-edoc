class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits=[]
        letters=[]
        for lst in logs:
            if lst.split()[1].isdigit():
                digits.append(lst)
            else:
                letters.append(lst)
        
        letters.sort(key = lambda x: (x.split()[1:],x.split()[0]))           
        result = letters + digits                                        
        return result
