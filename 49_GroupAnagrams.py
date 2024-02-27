# Time: O(m * n)
# Space: O(m+n); O(n) for dict, O(m) for the char

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            ch = [0] * 26
            for c in s:
                ch[ord(c) - ord('a')] += 1
            hm[tuple(ch)].append(s)
        return hm.values()
