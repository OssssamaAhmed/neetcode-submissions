class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for x in s:
            countS[x] = countS.get(x, 0) + 1

        for y in t:
               countT[y] = countT.get(y, 0) + 1

        return countS == countT   

            
        