class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        str_s = {}
        str_t = {}

        for x in s:
            str_s[x] = str_s.get(x, 0) + 1

        for y in t:
            str_t[y] = str_t.get(y, 0) + 1

        final_result = str_s == str_t

        return final_result







            
        