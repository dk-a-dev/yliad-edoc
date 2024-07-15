class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        rootNodesP1=[]
        childNodes=[]
        root=0
        main=[]
        extra=[]

        for i in descriptions:
            rootNodesP1.append(i[0])
            childNodes.append(i[1])

        for i in rootNodesP1:
            if i not in childNodes:
                root=i
                main.append(root)
                break

        for i in descriptions:
            if i[0]==root:
                main.append(i[1])

        for j in main:
            if j==root:
                continue
            else:
                for m in descriptions:
                    if m[0]==j:
                        extra.append(m[1])
            
        print(main+extra)
                