# Time: O(nlogn) , Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time: O(n) , Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_arr = [0] * 26
        t_arr = [0] * 26
        for i in range(len(s)):
            s_arr[ord(s[i]) - ord('a')] += 1
            t_arr[ord(t[i]) - ord('a')] += 1
        return s_arr == t_arr

# Time: O(n) , Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
