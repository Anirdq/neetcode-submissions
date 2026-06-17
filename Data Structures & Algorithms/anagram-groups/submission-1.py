class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i in strs:
            A = "".join(sorted(i))
            if A not in map:
                map[A]=[i]
            else:
                map[A].append(i)
        return list(map.values())

        