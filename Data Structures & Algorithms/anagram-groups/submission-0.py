class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(s)):
            j=''.join(sorted(s[i]))
            if j not in d:
                d[j]=[s[i]]
            else:
                d[j].append(s[i])
        return list(d.values())
