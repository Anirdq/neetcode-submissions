class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        xd={}
        for i in strs:
            A="".join(sorted(i))
            if A not in xd:
                xd[A]=[i]
            else:
                xd[A].append(i)
        return list(xd.values())

        